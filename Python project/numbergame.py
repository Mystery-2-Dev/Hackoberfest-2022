//intialization
var doors = [];

var toggle = function toggle(val){
	if(val == "closed")
		return "open"
	else
		return "closed";
}

//close all the doors
for (var i = 1; i<=100; i++){
	doors.push("closed");
}

//make the pass
for ( var rounds = 1; rounds <=100; rounds++){
	
	for(var i = 1; i <= 100; i++){
		if(i%rounds ==0){
			doors[i] = toggle(doors[i]);
		}
	}

}

//check the doors
for(var i = 1 ;i<=100; i++){
	console.log(doors[i]+" "+i);
}
