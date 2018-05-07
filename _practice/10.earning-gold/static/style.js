"use strict";
// **** jQuery *****
$(document).ready(function(){
	console.log("document ready for jQuery");
	$('body').css({
		'width':'785px'
		,'height':'330px'
		,'padding':'5px'
		// ,'border':'1px solid black'
		,'margin':'auto'
	})
	$('#top').css({
		'margin':'0px 10px'
	})
	$('#info').css({
		'border':'1px solid black'
		,'display':'inline-block'
		,'width':'80px'
	})
	$('form').css({
		'border':'1px solid black'
		,'width': '170px'
		,'height':'140px'
		,'margin':'5px'
		,'text-align':'center'
		,'display':'inline-block'
	});
	$('#area').css({
		'margin':'10px 5px'
		,'resize':'none'
		,'overflow':'auto'
	})

});
