"use strict";
// **** jQuery *****
$(document).ready(function(){
	console.log("document ready for jQuery");

	$('body').css({
		'padding':'30px'
		,'margin':'20px auto'
		,'border':'1px black solid'
		,'width': '350px'
		,'height': '270px'
	});
	$('input, button').css({
		'float':'right'
	})
	$('textarea').css({
		'resize':'none'
		,'height':'60px'
		,'display':'block'
		,'inline-height':'height'
		,'margin':'10px 10px 0px 0px'
	})
	$('#left,#right').css({
		'display':'inline-block'
		,'vertical-align':'top'
	})
	$('#left').css({
		'width':'80px'
		,'padding':'0px 0px 0px 20px'
	})
	$('#right').css({
		'width':'220px'
	})
	$('#right p').css({
		'margin':'0px'
		,'word-wrap': 'break-word'
	})
	$('#right>#comment').css({
		'overflow':'auto'
		,'height':'120px'
	})
	$('h3').css({
		'text-decoration': 'underline'
	})
});
