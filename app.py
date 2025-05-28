from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from questions import questions
import random

print(f"Cargadas {len(questions)} preguntas en total")

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure random key in production

@app.route('/')
def index():
    """Home page with mode selection"""
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    """Initialize the quiz based on selected mode"""
    mode = request.form.get('mode')
    
    # Reset session data
    session.clear()
    
    # Create indices list and shuffle them
    all_question_indices = list(range(len(questions)))
    random.shuffle(all_question_indices)
    
    # Select questions based on mode
    if mode == '40':
        # Take only 40 questions or all if less than 40
        selected_indices = all_question_indices[:min(40, len(questions))]
        session['mode'] = 'Simulacro de Examen'
    else:
        selected_indices = all_question_indices
        session['mode'] = 'Responde a Todas las Preguntas'
    
    # Store question indices instead of the full questions
    session['question_indices'] = selected_indices
    session['current_question'] = 0
    session['correct_answers'] = 0
    session['incorrect_answers'] = 0
    session['total_questions'] = len(selected_indices)
    
    # Debug info
    print(f"Total questions available: {len(questions)}")
    print(f"Selected questions: {len(selected_indices)}")
    
    # Ensure session is saved
    session.modified = True
    
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    """Show the quiz page"""
    # Check if quiz is properly initialized
    if 'question_indices' not in session:  # Cambiado de 'questions' a 'question_indices'
        return redirect(url_for('index'))
    
    return render_template('quiz.html', 
                          mode=session['mode'],
                          current=session['current_question'] + 1,
                          total=session['total_questions'],
                          correct=session['correct_answers'],
                          incorrect=session.get('incorrect_answers', 0))

@app.route('/get_question')
def get_question():
    """Return the current question data with randomized options"""
    if 'question_indices' not in session:
        return jsonify({"error": "Quiz not initialized"}), 400
    
    # Verify we have questions
    if not session.get('question_indices') or len(session['question_indices']) == 0:
        return jsonify({
            "error": "No hay preguntas disponibles",
            "completed": True
        }), 400
    
    current_idx = session['current_question']
    
    # Check if we've reached the end of the quiz
    if current_idx >= session['total_questions']:
        return jsonify({
            "completed": True,
            "correct": session['correct_answers'],
            "incorrect": session.get('incorrect_answers', 0),
            "total": session['total_questions']
        })
    
    # Get the actual question using the stored index
    question_index = session['question_indices'][current_idx]
    question_data = questions[question_index]
    
    # Rest of the function remains the same - randomize options, etc.
    # But store the index of the correct answer for this specific question
    options = question_data["options"].copy()
    correct_index = question_data["correct"]
    
    # Create a list of pairs (option, is_correct)
    option_pairs = [(options[i], i == correct_index) for i in range(len(options))]
    random.shuffle(option_pairs)
    
    # Unpack the shuffled pairs
    shuffled_options = [pair[0] for pair in option_pairs]
    new_correct_index = next(i for i, pair in enumerate(option_pairs) if pair[1])
    
    # Store the new correct index in the session
    session[f'correct_idx_{current_idx}'] = new_correct_index
    session.modified = True
    
    # Send response data
    response_data = {
        "question": question_data["question"],
        "options": shuffled_options
    }
    
    return jsonify(response_data)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    """Check if the answer is correct"""
    if 'question_indices' not in session:
        return jsonify({"error": "Quiz not initialized"}), 400
    
    data = request.get_json()
    selected_option = data.get('selected')
    current_idx = session['current_question']
    
    # Get the correct answer from the session
    correct_option = session.get(f'correct_idx_{current_idx}')
    
    is_correct = selected_option == correct_option
    
    if is_correct:
        session['correct_answers'] += 1
    else:
        session['incorrect_answers'] = session.get('incorrect_answers', 0) + 1
    
    # Move to next question
    session['current_question'] += 1
    session.modified = True
    
    return jsonify({
        "correct": is_correct,
        "correctOption": correct_option,
        "nextQuestion": session['current_question'] < session['total_questions']
    })

@app.route('/results')
def results():
    """Show the final results"""
    if 'question_indices' not in session:
        return redirect(url_for('index'))
    
    # Calculate score (0-10 scale, allowing negatives)
    correct = session['correct_answers']
    incorrect = session.get('incorrect_answers', 0)
    total = session['total_questions']
    
    # Formula: (correct - incorrect*0.5) / total * 10
    # Removed the max() function to allow negative scores
    raw_score = correct - (incorrect * 0.5)
    final_score = (raw_score / total) * 10
    
    return render_template('quiz.html', 
                          mode=session['mode'],
                          current=session['total_questions'],
                          total=session['total_questions'],
                          correct=session['correct_answers'],
                          incorrect=session.get('incorrect_answers', 0),
                          final_score=round(final_score, 2),
                          completed=True)

if __name__ == '__main__':
    app.run(debug=True)