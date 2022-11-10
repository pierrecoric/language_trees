//Language Trees
//just the beginning of an idea
//Pierre Coric

//initialise some variables
let margins = 200;
let longestWord = 0;
let xCoor = [];
let yCoor = [];
let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

//let rawText = 'A Polylith is a fluid-structure it doesn t exist  but it s already here  somewhere among us it is built to collectively invent and spread new stories it is a tool which usages lay in the process of making it as well as in its final form it is made in collaboration with active and passive humans and non humans actors of a specific place polyliths builders accept the inevitable decay of their structure as well as their constant evolution this inevitable decay followed by the final disintegration of the structure is only seen by the Polyliths builders as an opportunity to spread and re crystallize later in some other time and space only a community can pretend to own a polylith. As Language, it only exists spread among each of us nobody could ever grasp all the elements of a polylith hence polyliths never always fully exist ';
let rawText = 'come wayward souls that wander through the darkness there is a light for the lost and the meek  a'
let listText = [];
let currentWordText = '';

function setup() {
	//loop to populate the array listText from the raw text.
	for (let i = 0; i < rawText.length; i++) {
		if (rawText[i] != ' ' && rawText[i] != '\n' && rawText[i] != '\'') {
			currentWordText += rawText[i];
		}
		else {
			listText.push(currentWordText);
			currentWordText = '';
		}
	}
	//detect the longest word in the text
	for (let i = 0; i < listText.length; i++) {
		if (listText[i].length > longestWord) {
			longestWord = listText[i].length;
		}
	}
	//define the width and height of the drawing zone.
	widthCanvas = 8000;
	heightCanvas = 2000;
	createCanvas(widthCanvas,heightCanvas);
	//account for margins
	let widthArea = widthCanvas - 2*margins;
	let heightArea = heightCanvas - 2*margins;
	background(255);
	//divide the area horizontally according to the longest word 
	for (let i = 1; i <= longestWord; i++) {
		console.log(i);
		xCoor.push(margins + (i-1)*(widthArea/(longestWord-1)));
		console.log(xCoor[i-1]);
	}
	//dividce the area vertically according to the alphabet
	for (let i = 1; i <= 26; i ++) {
		yCoor.push(margins + (i-1)*(heightArea/(26-1)));
	}
	//function to draw the height of each letter
	twentySix();
	//call the function to draw the node for each word of the text
	for (let i = 0; i < listText.length; i ++) {
		drawNodes(listText[i]);
	}
	//save the picture
	save('ok.jpg');
}

//nothing is looping here
function draw() {
}

//function to draw the height of each letter of the alphabet for each column
function twentySix() {
	for (let i = 0; i < longestWord; i++) {
		for (let a = 0; a < 26; a ++) {
			ellipse(xCoor[i], yCoor[a], 10,10);
		}
	}
}

//draw the nodes for each word
function drawNodes(word) {
	let firstCoor = 0;
	let secondCoor = 0;
	for (let i = 1; i < word.length; i++) {
		for (let a = 0; a < 26; a++) {
			if (word[i-1] == alphabet[a]) {
				firstCoor = a;
			}
			if (word[i] == alphabet[a]) {
				secondCoor = a;
			}
		}
		strokeWeight(4);
		//stroke(255,255,255,255);
		//fill(255,255,255,255);
		stroke(0,0,0,255);
		fill(0,0,0, 255);
		line(xCoor[i-1],yCoor[firstCoor], xCoor[i], yCoor[secondCoor]);
		ellipse(xCoor[i-1], yCoor[firstCoor], 24, 24);
		ellipse(xCoor[i], yCoor[secondCoor], 24, 24);
	}
}