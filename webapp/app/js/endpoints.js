function inicializarContenidos() {
  listarMensajes();
  listarFotos();
}

function listarMensajes() {
  var request = gapi.client.bodaAbejorrosAPI.bodaabejorros.listarMensajes();
  request.execute(function(resp) {
    for (var m in resp.items) {
      var mensajeRecibido = new MensajeModel(resp.items[m].nombre,
        resp.items[m].email,resp.items[m].mensaje,resp.items[m].fecha);
      model.mm.addMensaje(mensajeRecibido);
    }
  });
}

function listarFotos() {
  var request = gapi.client.bodaAbejorrosAPI.bodaabejorros.listarFotos();
  request.execute(function(resp) {
    for (var f in resp.items) {
      var fotoRecibida = new FotoModel(resp.items[f].categoria,
        resp.items[f].titulo,resp.items[f].descripcion,resp.items[f].url,resp.items[f].fecha);
      model.fm.addFoto(fotoRecibida);
      console.log(fotoRecibida);
    }
  });
}

var Model = function(mensajesModel,fotosModel) {
  this.mm = mensajesModel;
  this.fm = fotosModel;
}

// Initializing knockout js mensajes model
var MensajesModel = function(mensajes) {
  this.mensajes = ko.observableArray(mensajes);
  this.addMensaje = function(msg) {
    this.mensajes.push(msg);
  }
}

var MensajeModel = function(nombre,email,msg,fecha) {
  this.nombre = nombre;
  this.email = email;
  this.mensaje = msg;
  this.fecha = fecha;
}

// Initializing knockout js mensajes model
var FotosModel = function(fotos) {
  this.fotos = ko.observableArray(fotos);
  this.addFoto = function(f) {
    this.fotos.push(f);
  }
}

var FotoModel = function(categoria,titulo,descripcion,url,fecha) {
  this.categoria = categoria;
  this.titulo = titulo;
  this.descripcion = descripcion;
  this.url = url;
  this.fecha = fecha;
}

function init() {
  console.log('initializing endpoints');

  mensajesModel = new MensajesModel([]);
  fotosModel = new FotosModel([]);
  model = new Model(mensajesModel,fotosModel);

  var ROOT = 'https://boda-abejorros.appspot.com/_ah/api';
  //var ROOT = '//' + window.location.host + '/_ah/api';
  gapi.client.load('bodaAbejorrosAPI', 'v1', function() {
    inicializarContenidos();
  }, ROOT); 

  ko.applyBindings(model);
  // ko.applyBindings(mensajesModel);
  // ko.applyBindings(fotosModel);

}

