"use strict";
// **** jQuery *****
$(document).ready(function(){
	$('body').on(function(){
		console.log("You are with the <body></body> element");
	})
	$('body').click(function(){
		alert("You just clicked.");
	})
	//GETTER
	$('h1').click(function(){
		console.log('h1');
	})
	//SETTER
	$('h1').click(function(){
		$('h1').text('jQuery set this.');
	})
});

// **** JavaScript *****
function sampleFunction (arr) {

  for(var i=0;i<arr.length;i++)
  {
    console.log(arr[i]);
  }  

  console.log("The input array of objects: "+arr);

}

var myLoc = { 'city': 'Dallas' };
var foo=[ true, null, ('version'+2.0), {'a_key':'a_value'}, myLoc ];

sampleFunction(foo);