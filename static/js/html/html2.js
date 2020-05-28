/*timer*/
  var minutesLabel = document.getElementById("minutes");
  var secondsLabel = document.getElementById("seconds");
  var totalSeconds = 0;
  setInterval(setTime, 1000);
  
  function setTime() {
    ++totalSeconds;
    secondsLabel.innerHTML = pad(totalSeconds % 60);
    minutesLabel.innerHTML = pad(parseInt(totalSeconds / 60));

  }

  
  function pad(val) {
    var valString = val + "";
    if (valString.length < 2) {
      return "0" + valString;
    } else {
      return valString;
    }
  }
  

/*ajax call*/

var questions = [];
  $.ajax({
    url: 'http://127.0.0.1:8000/api2/?format=json',
    type:'GET',
    async:true,
    dataType: "json",
    success: function(data)
     {
        questions = data ;
        loadQuestion();
        
     }
});



//Displaying questions
  var currentQuestion = 0;
  var score = 0;
  var totQuestions = 8;
  var AnswerOption = null;
  
  function loadQuestion() 
  {

    
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
    
    if(1 == parseInt(questions[currentQuestion].answer)) AnswerOption = opt1;
    if(2 == parseInt(questions[currentQuestion].answer)) AnswerOption = opt2;
    if(3 == parseInt(questions[currentQuestion].answer)) AnswerOption = opt3;
    if(4 == parseInt(questions[currentQuestion].answer)) AnswerOption = opt4;
  } 
  
  //Loading next question
  function loadNextQuestion() {
    resetColor();
    enableAll();
    var selectedOption = document.querySelector('input[type=radio]:checked');
    if (!selectedOption) {
      alert('Please select your answer!');
      return;
    }
    var answer = selectedOption.value;
    if (questions[currentQuestion].answer == answer) {
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
    var timeCont = document.getElementById('counter');
    var statusCont = document.getElementById('status');
    var homeCont = document.getElementById('home');
    var nameCont=document.getElementById('name');
     var scoresaver = document.getElementById('scoresaver');
    if (currentQuestion == totQuestions) {
      container.style.display = 'none';
      resultCont.style.display = '';
      timeCont.style.display='';
      statusCont.style.display='';
      homeCont.style.display='';
      nameCont.style.display='';
      scoresaver.style.display='';


      localStorage.setItem('scores',score)
      var scoress = localStorage.getItem('scores')

      if(score == 0 || score < 40)
      {
          resultCont.innerHTML = 'Your Score:- ' + score + '/80' ;
          timeCont.innerHTML = 'Time taken :' + 'Min:' + minutesLabel.textContent + ':'  + 'Sec:' + secondsLabel.textContent ;
          statusCont.innerHTML = "Status: FAIL";
          homeCont.innerHTML =  "<a href ="/" onclick='scoresubmit()'>Submit the score and share the results</a>";
          scoresaver.innerHTML = "<button onclick='scoresubmit()'>Submit</button>";
        }
      
      else {
        resultCont.innerHTML = 'Your Score:- ' + score + '/80' ;
          timeCont.innerHTML = 'Time taken :' + 'Min:' + minutesLabel.textContent + ':'  + 'Sec:' + secondsLabel.textContent ;
          statusCont.innerHTML = "Status: PASS";
          homeCont.innerHTML =  "<a href ="/" onclick='scoresubmit()'>Submit the score and share the results</a>";
          scoresaver.innerHTML = "<button onclick='scoresubmit();'>Submit</button>";

        }

        
      return;
    }
    
  
    loadQuestion(currentQuestion);
  }


  
  //checking answers
  function check() {
    resetColor();
    var selectedOption = document.querySelector('input[type=radio]:checked');
    if (selectedOption == AnswerOption) {
      selectedOption.parentNode.style.backgroundColor = "green";
      nextButton.innerHTML = 'Next';

    } else {
      selectedOption.parentNode.style.backgroundColor = "red";
      AnswerOption.parentNode.style.backgroundColor = "green";
      nextButton.style.backgroundColor = "white";
      nextButton.innerHTML = 'Next';

    }
    disableAll();
  }
  
  //bg color disabled for each option after the next button clicked
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
  
  //reset color and next button
  function resetColor(){
    let options = document.querySelectorAll("input[type=radio]");
    for(let i = 0; i < options.length; ++i){
      options[i].parentNode.style.background = "none";
      nextButton.style.background = "none";
      nextButton.innerHTML = '';


    }
  }
  
  
  loadQuestion(currentQuestion);

// var id_score = document.getElementById('id_score');
//   function scoresubmit(){
//   $.ajax({
//     url: '/',
//     method : 'POST',
//     data: {score: $('#result').val(), "csrfmiddlewaretoken" : "{{csrf_token}}"},
//     success: function(data) {

//       $('#id_score').html(data.parentNode);
//       console.log(data.score.value);
//     }
//      });

//     }


    function scoresubmit(){
      $.ajax({
        url: "/",
        method : 'POST',
        data: {
          score: $('#result').val(), 
          "csrfmiddlewaretoken" : "{{csrf_token}}"
        },
        success: function() {
          $('#score').html(score);
        }
         });
        }