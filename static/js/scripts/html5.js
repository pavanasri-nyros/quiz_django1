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
  url: 'http://quizdjango1.herokuapp.com/api5/?format=json',
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
  var headingCont = document.getElementById('heading');
  var quiznameCont = document.getElementById('quizname');
  var resultCont = document.getElementById('result');
  var timeCont = document.getElementById('counter');
  var statusCont = document.getElementById('status');
  var shareCont = document.getElementById('share');
  if (currentQuestion == totQuestions) {
    container.style.display = 'none';
    headingCont.style.display = '';
    quiznameCont.style.display='';
    resultCont.style.display = '';
    timeCont.style.display='';
    statusCont.style.display='';
    shareCont.style.display='';

    if(score == 0 || score < 40)
    {
        headingCont.innerHTML = '<h1>Result</h1>';
        quiznameCont.innerHTML = "<span id='quiznames'>CSS Quiz1 </span>";
        timeCont.innerHTML = 'Time taken :' + 'Min:' + minutesLabel.textContent + ':'  + 'Sec:' + secondsLabel.textContent ;
        statusCont.innerHTML = "Status:<span id='report'> FAIL</span>";
        resultCont.innerHTML = "<div><h3>Your Score:- "+ score +" /80</h3><input type='text' class='form-controlname' id='name' placeholder='Enter Name'> <button onclick='scoresubmit()' id='scoresubmit' class='btn btn-secondary'>Submit Score</button></div>" ;
        shareCont.innerHTML = "<div class='fb-share-button' data-href='https://herokuapp.quiz_django1.com/' data-layout='button_count' data-size='large'><a target='_blank' href='https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;src=sdkpreparse' class='fb-xfbml-parse-ignore'>Share</a></div>";
      }
    
    else {
        headingCont.innerHTML = '<h1>Result</h1>';
        quiznameCont.innerHTML = "<span id='quiznames'>CSS Quiz1 </span>";
        timeCont.innerHTML = 'Time taken :' + 'Min:' + minutesLabel.textContent + ':'  + 'Sec:' + secondsLabel.textContent ;
        statusCont.innerHTML = "Status:<span id='report'>PASS</span>";
        resultCont.innerHTML = "<div><h3>Your Score:- "+ score +" /80</h3><input type='text' class='form-controlname' id='name' placeholder='Enter Name'> <button onclick='scoresubmit()' id='scoresubmit' class='btn btn-secondary'>Submit Score</button></div>" ;
        shareCont.innerHTML = "<div class='fb-share-button' data-href='https://herokuapp.quiz_django1.com/' data-layout='button_count' data-size='large'><a target='_blank' href='https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;src=sdkpreparse' class='fb-xfbml-parse-ignore'>Share</a></div>";
   
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


  function scoresubmit(){
    var scores= score;
    var name = $('#name').val()
    var status = $('#report').text()
    var quizname = $('#quiznames').text()

    $.ajax({
      url: '',
      data: {
        'scores':scores ,
        'name':name,
        'status':status,
        'quizname':quizname,
         },
      success: function(data) {
        alert('successfully submitted the score Now you can share the score to scoial media');

      }
       });
      }