// var counter = 0;
// var timeleft = 300;



// function setup(){

//     var timer =  document.getElementById('timer');
//     timer.innerHTML = convertSeconds(timeleft - counter);
//     function timeIt(){
//         counter++;
//         timer.innerHTML =convertSeconds(timeleft - counter);

//     }
//     setInterval(timeIt, 1000);

//     var params = getURLParams();
//     if(params.minute){
//         var min = params.minute;
//         timeleft = min * 60;
//     }
// }

// function convertSeconds(s){
//     var min = Math.floor(s / 60);
//     var sec = s % 60;
//     return min + ':' + sec;
// }


// setup();


// var timerInterval;

// function timeIt(){
//     counter++;
//     if(timeleft - counter <= 0){
//         clearInterval(timerInterval);
//         timer.innerHTML = convertSeconds(0);
//         displayResults();
//     }
//     else {
//         timer.innerHTML = convertSeconds(timeleft - counter);
//     }    
// }

// timerInterval = setInterval(timeIt, 1000);


