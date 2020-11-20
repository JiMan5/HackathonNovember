	function Chosen(){
		var element = -1;
	}

	function chooseEvent(element){
		var objDiv = document.getElementById("info-section");

		objDiv.scrollTop = 0;


		document.getElementById('info-section').style.marginRight = '0px';
		document.getElementById('info-section-title').innerHTML = element[4];

		document.getElementById('host').innerHTML ="Host: " + element[0];

		number = element[6];
		address = element[2].replace(/ /g,"+");
		city = element[7];
		TN =element[8];

		document.getElementById('location').innerHTML = "Address:" + " " + element[2] + " " + number ;

		document.getElementById('location').href = 'http://maps.google.com/maps?q=' + number + "+" + address + ",+" + city + ',+TN+' + TN;

		document.getElementById('calendar').innerHTML ="Date: " + element[1];

		document.getElementById('type').innerHTML ="Type: " + element[3].substring(0,element[3].length-4);

		document.getElementById('info-section-text').innerHTML = element[5];

		document.getElementById('myBar').style.width = (element[9]/element[10])*100 + '%';

		Chosen.element = element;

	}

	function closeThis(){
		document.getElementById('info-section').style.marginRight = '-600px';
	}

	var joined = false;
	function clickJoin(){
		if(joined){
			document.getElementById('Join').innerHTML = 'Join';
			document.getElementById('Join').style.transition = '0s';
			document.getElementById('Join').style.padding = '20px 53px';
			document.getElementById('myBar').style.transition = '0.7s';
			document.getElementById('myBar').style.width = (Chosen.element[9]/Chosen.element[10])*100 + '%';
			joined = false;

			var objDiv = document.getElementById("info-section");

			objDiv.scrollTop = 0;
		}

		else if(Chosen.element[9]<Chosen.element[10]){
			document.getElementById('Join').innerHTML = 'Leave';
			document.getElementById('Join').style.transition = '0s';
			document.getElementById('Join').style.padding = '20px 46px';
			document.getElementById('myBar').style.transition = '0.7s';
			document.getElementById('myBar').style.width = ((Chosen.element[9]+1)/Chosen.element[10])*100 + '%';
			joined = true;
			var objDiv = document.getElementById("info-section");

			objDiv.scrollTop = objDiv.scrollHeight;
		}
	}