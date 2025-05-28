document.addEventListener('DOMContentLoaded', function() {
    // Only execute on quiz page
    const questionContainer = document.getElementById('question-container');
    if (!questionContainer) return;

    const questionText = document.getElementById('question-text');
    const optionsContainer = document.getElementById('options-container');
    const feedbackContainer = document.getElementById('feedback-container');
    const feedbackText = document.getElementById('feedback-text');
    const nextBtn = document.getElementById('next-btn');
    const currentQuestionElement = document.getElementById('current-question');
    const correctAnswersElement = document.getElementById('correct-answers');
    const incorrectAnswersElement = document.getElementById('incorrect-answers');

    let selectedOption = null;
    
    // Load the first question
    loadQuestion();

    // Add event listener for next button
    nextBtn.addEventListener('click', loadQuestion);

    // Load question function
    function loadQuestion() {
        // Hide feedback and next button
        feedbackContainer.style.display = 'none';
        nextBtn.style.display = 'none';
        
        // Clear options
        optionsContainer.innerHTML = '';
        
        // Fetch the next question
        fetch('/get_question')
            .then(response => response.json())
            .then(data => {
                if (data.completed) {
                    // Quiz is completed, redirect to results
                    window.location.href = '/results';
                    return;
                }
                
                // Display the question
                questionText.textContent = data.question;
                
                // Create and display the options
                data.options.forEach((option, index) => {
                    const optionBtn = document.createElement('button');
                    optionBtn.className = 'option-btn';
                    optionBtn.textContent = option;
                    optionBtn.dataset.index = index;
                    
                    optionBtn.addEventListener('click', function() {
                        if (selectedOption !== null) return; // Prevent multiple selections
                        
                        selectedOption = index;
                        checkAnswer(index);
                    });
                    
                    optionsContainer.appendChild(optionBtn);
                });
            })
            .catch(error => {
                console.error('Error loading question:', error);
                questionText.textContent = 'Error cargando pregunta. Por favor, inténtalo de nuevo.';
            });
    }

    // Check the answer
    function checkAnswer(selectedIndex) {
        fetch('/check_answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ selected: selectedIndex })
        })
        .then(response => response.json())
        .then(data => {
            // Show the feedback
            feedbackContainer.style.display = 'block';
            
            if (data.correct) {
                feedbackText.textContent = '¡Correcto!';
                feedbackContainer.style.backgroundColor = '#d4edda';
                feedbackContainer.style.color = '#155724';
                
                // Update correct answers counter
                correctAnswersElement.textContent = parseInt(correctAnswersElement.textContent) + 1;
            } else {
                // Here's the fix - we reference correctly by index
                feedbackText.textContent = '¡Incorrecto! La respuesta correcta era: ' + 
                    optionsContainer.children[data.correctOption].textContent;
                feedbackContainer.style.backgroundColor = '#f8d7da';
                feedbackContainer.style.color = '#721c24';
                
                // Update incorrect answers counter
                if (incorrectAnswersElement) {
                    incorrectAnswersElement.textContent = parseInt(incorrectAnswersElement.textContent || 0) + 1;
                }
            }
            
            // Mark options as correct/incorrect
            Array.from(optionsContainer.children).forEach((option, index) => {
                option.disabled = true;
                
                if (index === data.correctOption) {
                    option.classList.add('option-correct');
                } else if (index === selectedIndex && !data.correct) {
                    option.classList.add('option-incorrect');
                }
            });
            
            // Show next button if there are more questions
            if (data.nextQuestion) {
                nextBtn.style.display = 'inline-block';
                
                // Update question counter
                currentQuestionElement.textContent = parseInt(currentQuestionElement.textContent) + 1;
                
                // Update progress bar
                const total = parseInt(document.getElementById('total-questions').textContent);
                const current = parseInt(currentQuestionElement.textContent);
                document.querySelector('.progress-fill').style.width = `${(current / total) * 100}%`;
            } else {
                // Quiz is complete, show results button
                nextBtn.textContent = 'Ver resultados';
                nextBtn.style.display = 'inline-block';
            }
            
            // Reset selected option
            selectedOption = null;
        })
        .catch(error => {
            console.error('Error checking answer:', error);
            feedbackContainer.style.display = 'block';
            feedbackText.textContent = 'Error al verificar respuesta. Por favor, inténtalo de nuevo.';
        });
    }
});