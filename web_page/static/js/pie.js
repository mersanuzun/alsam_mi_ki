window.onload = function () {
	var chart = new CanvasJS.Chart("chartContainer",
	{
		title:{
			text: "What other people think?",
			fontFamily: "arial black"
		},
                animationEnabled: true,
		legend: {
			verticalAlign: "bottom",
			horizontalAlign: "center"
		},
		theme: "theme1",
		data: [
		{        
			type: "pie",
			indexLabelFontFamily: "Garamond",       
			indexLabelFontSize: 20,
			indexLabelFontWeight: "bold",
			startAngle:0,
			indexLabelFontColor: "MistyRose",       
			indexLabelLineColor: "darkgrey", 
			indexLabelPlacement: "inside", 
			toolTipContent: "{name}: {y}hrs",
			showInLegend: true,
			indexLabel: "#percent%", 
			dataPoints: [
				{  y: 52, name: "It's good.", legendMarkerType: "triangle"},
				{  y: 44, name: "It'is bad.", legendMarkerType: "square"},
				{  y: 0, name: "Time Spent Out", legendMarkerType: "circle"}
			]
		}
		]
	});
	chart.render();
}
