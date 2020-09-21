//https://www.eclipse.org/paho/clients/js/

function LED1ENCENDIDO() {
	inttext1=document.getElementById("inttext1").value
	intclave1=document.getElementById("intclave").value
	message=new.Paho.MQTT.Message("led1encendida"+"inttext1"+"intclave1")
	message.destinationName="mdpilatuna.fie@unach.edu.ec/dispositivo";
	client.send(message);
}
function LED1APAGADO() {
	inttext2=document.getElementById("inttext1").value
	intclave2=document.getElementById("intclave").value
	message=new.Paho.MQTT.Message("led1apagada"+"inttext2"+"intclave2")
	message.destinationName="mdpilatuna.fie@unach.edu.ec/dispositivo";
	client.send(message);
}
function LED2ENCENDIDO() {
	inttext3=document.getElementById("inttext1").value
	intclave3=document.getElementById("intclave").value
	message=new.Paho.MQTT.Message("led2encendida"+"inttext3"+"intclave3")
	message.destinationName="mdpilatuna.fie@unach.edu.ec/dispositivo";
	client.send(message);
}
function LED2APAGADO() {
	inttext4=document.getElementById("inttext1").value
	intclave4=document.getElementById("intclave").value
	message=new.Paho.MQTT.Message("led2apagada"+"inttext4"+"intclave4")
	message.destinationName="mdpilatuna.fie@unach.edu.ec/dispositivo";
	client.send(message);
}

// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));

  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
   useSSL: false,
    userName: "mdpilatuna.fie@unach.edu.ec",
    password: "quitociudadhermosa",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);
   
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Conectando,espera mientras procesamos tu informacion...");
	
    client.subscribe("mdpilatuna.fie@unach.edu.ec/servidor");
    message = new Paho.MQTT.Message("hola desde la web");
    message.destinationName = "mdpilatuna.fie@unach.edu.ec/dispositivo";
    client.send(message);
	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    text=(message.payloadString);
	console.log(text)
	document.getElementById("respuesta").innerHTML=text;
	
  }
  
