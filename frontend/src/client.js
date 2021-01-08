//GET Request for list of questions from the server
let request = new XMLHttpRequest();

request.onreadystatechange = function(){	
	if(this.readyState == 4 && this.status == 200){ 
		questions = JSON.parse(this.responseText).questions;

		//Displays the new received questions
		for (let question in questions){
			let newquestion = document.createElement("li");
			newquestion.textContent = questions[question];
			document.getElementById("questions").appendChild(newquestion);
		}
		
	}
}
request.open("GET", "/questions", true);
request.setRequestHeader('Accept', 'application/json');
request.send();


let button = document.getElementById("button");
button.onclick = function(){
    console.log("Button was clicked");
}



function saveAnswer(answer){
	//POST Request to save the answers to the server
	let request = new XMLHttpRequest();

	request.onreadystatechange = function(){	
		if(this.readyState == 4 && this.status == 200){
			console.log(request.responseText);
		}
	}
	request.open("POST","/answer",true);
	request.setRequestHeader('Content-type', 'application/json');
	request.send(JSON.stringify({"answer":answer}));	
}


