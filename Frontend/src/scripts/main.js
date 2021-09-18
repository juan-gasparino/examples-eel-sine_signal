import main from '../UX/styles/main.scss';

function deactivateDevTool() {
	window.oncontextmenu = () => {
		return false;
	}
	document.onkeydown = (e) => {
		if (window.event.keyCode == 123 || e.button == 2)
			return false;
	}
}

function eventHandler() {

	let signalParams = {
		message: '',
		freq: 0
	}

	document.getElementById("message").addEventListener("change", (input) => {
		signalParams.message = input.target.value;
	});
	document.getElementById("freq").addEventListener("change", (input) => {
		signalParams.freq = +input.target.value;
	});
	document.getElementById("btn_sendMessage").addEventListener("click", (e) => {
		e.preventDefault();
		showSignal(signalParams);
	});

}

function showSignal(signalParams) {

	// eel.testing("testing eel")((data)=>{
	//     console.log(data)
	// });
	eel.main(signalParams);
}

//deactivateDevTool();
eventHandler();