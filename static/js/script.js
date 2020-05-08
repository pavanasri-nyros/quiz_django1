var questions = [];
  $.ajax({
    url: 'http://127.0.0.1:8000/api/?format=json',
    type:'GET',
    async:true,
    dataType: "json",
    success: function(data)
     {
        questions = data ;
        loadQuestion();
        
     }
});

  
  var currentQuestion = 0;
  var score = 0;
  var totQuestions = 8;
  var AnswerOption = null;
  
  function loadQuestion() {
    resetColor();
    enableAll();
    //questionIndex = 0
    var questionEl = document.getElementById("question");
    var opt1 = document.getElementById("opt1");
    var opt2 = document.getElementById("opt2");
    var opt3 = document.getElementById("opt3");
    var opt4 = document.getElementById("opt4");
  
    questionEl.innerHTML = (currentQuestion + 1) + '. ' + questions[currentQuestion].question;
    opt1.innerHTML = questions[currentQuestion].option1;
    opt2.innerHTML = questions[currentQuestion].option2;
    opt3.innerHTML = questions[currentQuestion].option3;
    opt4.innerHTML = questions[currentQuestion].option4;
    
    if(1 == parseInt(questions[currentQuestion].correct_answer)) AnswerOption = opt1;
    if(2 == parseInt(questions[currentQuestion].correct_answer)) AnswerOption = opt2;
    if(3 == parseInt(questions[currentQuestion].correct_answer)) AnswerOption = opt3;
    if(4 == parseInt(questions[currentQuestion].correct_answer)) AnswerOption = opt4;
  } 
  
  function loadNextQuestion() {
    resetColor();
    enableAll();
    var selectedOption = document.querySelector('input[type=radio]:checked');
    if (!selectedOption) {
      alert('Please select your answer!');
      return;
    }
    var answer = selectedOption.value;
    if (questions[currentQuestion].correct_answer == answer) {
      score += 10;
    }
  
    selectedOption.checked = false;
    currentQuestion++;
  
    var nextButton = document.getElementById('nextButton');
    if (currentQuestion == totQuestions - 1) {
      nextButton.innerHTML = 'Finish';
    }
  
    var container = document.getElementById('quizContainer');
    var resultCont = document.getElementById('result');
    if (currentQuestion == totQuestions) {
      container.style.display = 'none';
      resultCont.style.display = '';
      resultCont.innerHTML = 'Your Score: ' + score + '/80' + '<br>' + '<a href ="/">Home</a>' ;


      return;
    }
   

    loadQuestion(currentQuestion);
  }
  
  function check() {
    resetColor();
    var selectedOption = document.querySelector('input[type=radio]:checked');
    if (selectedOption == AnswerOption) {
      selectedOption.parentNode.style.backgroundColor = "green";
    } else {
      selectedOption.parentNode.style.backgroundColor = "red";
      AnswerOption.parentNode.style.backgroundColor = "green";
    }
    disableAll();
  }
  
  function disableAll(){
    let options = document.querySelectorAll("input[type=radio]");
    for(let i = 0; i < options.length; ++i){
      options[i].setAttribute("disabled","true");
    }
  }
  
  function enableAll(){
    let options = document.querySelectorAll("input[type=radio]");
    for(let i = 0; i < options.length; ++i){
      options[i].removeAttribute("disabled");
    }
  }
  
  
  function resetColor(){
    let options = document.querySelectorAll("input[type=radio]");
    for(let i = 0; i < options.length; ++i){
      options[i].parentNode.style.background = "none";
    }
  }
  
  
  loadQuestion(currentQuestion);




