"use strict";
// **** jQuery *****
$(document).ready(function(){
	console.log("document ready for jQuery");

	$('body').css({
		'margin':'30px auto'
		,'width': '600px'
		,'text-align':'center'
	});
	$('form').css({
		'width':'200px'
		,'margin':'auto'
	});
	$('#win').css({
		'background-color':'green'
		,'padding':'10px'
		,'height':'150px'
	});
	$('#info').css({
		'background-color':'red'
		,'color':'white'
		,'padding':'40px'
		,'margin':'10px 140px'
	});

});
