from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from questions import questions
import random

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
    
    # Create a copy of questions and shuffle them
    all_questions = questions.copy()
    random.shuffle(all_questions)
    
    # Select questions based on mode
    if mode == '40':
        # Take only 40 questions or all if less than 40
        selected_questions = all_questions[:min(40, len(all_questions))]
        session['mode'] = '40 Questions'
    else:
        selected_questions = all_questions
        session['mode'] = 'All Questions'
    
    # Store questions in session
    session['questions'] = selected_questions
    session['current_question'] = 0
    session['correct_answers'] = 0
    session['incorrect_answers'] = 0  # Track incorrect answers
    session['total_questions'] = len(selected_questions)
    
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    """Show the quiz page"""
    # Check if quiz is properly initialized
    if 'questions' not in session:
        return redirect(url_for('index'))
    
    return render_template('quiz.html', 
                          mode=session['mode'],
                          current=session['current_question'] + 1,
                          total=session['total_questions'],
                          correct=session['correct_answers'],
                          incorrect=session.get('incorrect_answers', 0))  # Pass incorrect count

@app.route('/get_question')
def get_question():
    """Return the current question data with randomized options"""
    if 'questions' not in session:
        return jsonify({"error": "Quiz not initialized"}), 400
    
    current_idx = session['current_question']
    
    # Check if we've reached the end of the quiz
    if current_idx >= session['total_questions']:
        return jsonify({
            "completed": True,
            "correct": session['correct_answers'],
            "incorrect": session.get('incorrect_answers', 0),
            "total": session['total_questions']
        })
    
    # Get current question
    question_data = session['questions'][current_idx]
    
    # Get original options and correct answer index
    options = question_data["options"].copy()
    correct_index = question_data["correct"]
    correct_answer = options[correct_index]  # Store the correct answer text
    
    # Create a list of pairs (option, is_correct)
    option_pairs = [(options[i], i == correct_index) for i in range(len(options))]
    
    # Shuffle the pairs
    random.shuffle(option_pairs)
    
    # Unpack the shuffled pairs
    shuffled_options = [pair[0] for pair in option_pairs]
    
    # Find the new index of the correct answer
    new_correct_index = next(i for i, pair in enumerate(option_pairs) if pair[1])
    
    # Store the new correct index and answer text in the session
    # Make a copy to avoid modifying the original
    updated_question = dict(question_data)
    updated_question['shuffled_correct'] = new_correct_index
    updated_question['correct_answer_text'] = correct_answer
    session['questions'][current_idx] = updated_question
    
    # Mark the session as modified
    session.modified = True
    
    # Send response data
    response_data = {
        "question": question_data["question"],
        "options": shuffled_options
    }
    
    return jsonify(response_data)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    """Check if the answer is correct using the shuffled index"""
    if 'questions' not in session:
        return jsonify({"error": "Quiz not initialized"}), 400
    
    data = request.get_json()
    selected_option = data.get('selected')
    
    current_idx = session['current_question']
    current_question = session['questions'][current_idx]
    
    # Use the shuffled correct index
    correct_option = current_question.get('shuffled_correct', current_question['correct'])
    
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
    if 'questions' not in session:
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