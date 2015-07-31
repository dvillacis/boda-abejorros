"""Hello World API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""


import endpoints
import datetime

from google.appengine.ext import ndb
from protorpc import messages
from protorpc import message_types
from protorpc import remote


package = 'BodaAbejorros'

class Mensaje(ndb.Model):
    """Aqui se almacenan los mensajes que nos dejan."""
    nombre = ndb.StringProperty()
    email = ndb.StringProperty()
    fecha = ndb.DateTimeProperty(auto_now_add=True)
    mensaje = ndb.StringProperty()

class Asistente(ndb.Model):
    """Aqui se almacenan los asistentes confirmados y los eventos"""
    nombre = ndb.StringProperty()
    email = ndb.StringProperty()
    mensaje = ndb.StringProperty()
    requerimientos = ndb.StringProperty()
    fecha = ndb.DateTimeProperty(auto_now_add=True)
    eventos = ndb.StringProperty()

class Foto(ndb.Model):
    """Este es el modelo de la fotografia"""
    categoria = ndb.StringProperty()
    titulo = ndb.StringProperty()
    descripcion = ndb.StringProperty()
    url = ndb.StringProperty()
    fecha = ndb.DateTimeProperty(auto_now_add=True)

class MensajeResponse(messages.Message):
    email = messages.StringField(1)
    nombre = messages.StringField(2)
    fecha = messages.StringField(3)
    mensaje = messages.StringField(4)

class MensajeCollectionResponse(messages.Message):
    items = messages.MessageField(MensajeResponse, 1, repeated=True)

class AsistenteResponse(messages.Message):
    email = messages.StringField(1)
    nombre = messages.StringField(2)
    fecha = messages.StringField(3)
    mensaje = messages.StringField(4)
    requerimientos = messages.StringField(5)
    eventos = messages.StringField(6)

class AsistenteCollectionResponse(messages.Message):
    items = messages.MessageField(AsistenteResponse, 1, repeated=True)

class FotoResponse(messages.Message):
    categoria = messages.StringField(1)
    titulo = messages.StringField(2)
    descripcion = messages.StringField(3)
    url = messages.StringField(4)
    fecha = messages.StringField(5)

class FotoCollectionResponse(messages.Message):
    items = messages.MessageField(FotoResponse, 1, repeated=True)


@endpoints.api(name='bodaAbejorrosAPI', version='v1')
class BodaAbejorrosAPI(remote.Service):
    """BodaAbejorros API v1."""

    #listar todos los mensajes
    @endpoints.method(message_types.VoidMessage, MensajeCollectionResponse,
        path='listarMensajes', http_method='GET', name='bodaabejorros.listarMensajes')
    def bodaabejorros_listarMensajes(self,request):
        mcr = MensajeCollectionResponse()
        qry = Mensaje.query()
        for q in qry:
            f = q.fecha.strftime("%Y-%m-%d %H:%M:%S")
            mensajeRecibido = MensajeResponse(email=q.email,nombre=q.nombre,fecha=f,mensaje=q.mensaje)
            mcr.items.append(mensajeRecibido)
        return mcr

    #Defino el recurso mensaje
    MENSAJE_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        nombre=messages.StringField(2,variant=messages.Variant.STRING),
        email=messages.StringField(3,variant=messages.Variant.STRING),
        mensaje=messages.StringField(4,variant=messages.Variant.STRING))

    #guardar un mensaje
    @endpoints.method(MENSAJE_RESOURCE, MensajeCollectionResponse,
        path='guardarMensaje', http_method='POST', name='bodaabejorros.guardarMensaje')
    def boda_abejorros_guardarMensaje(self,request):
        msg = Mensaje(nombre=request.nombre,email=request.email,mensaje=request.mensaje)
        msg.put()
        f = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mcr = MensajeCollectionResponse()
        mcr.items.append(MensajeResponse(email=request.email,nombre=request.nombre,fecha=f,mensaje=request.mensaje))
        qry = Mensaje.query()
        for q in qry:
            f = q.fecha.strftime("%Y-%m-%d %H:%M:%S")
            mensajeRecibido = MensajeResponse(email=q.email,nombre=q.nombre,fecha=f,mensaje=q.mensaje)
            mcr.items.append(mensajeRecibido)
        return mcr

    #listar todos los asistentes al evento
    @endpoints.method(message_types.VoidMessage, AsistenteCollectionResponse,
        path='listarAsistentes', http_method='GET', name='bodaabejorros.listarAsistentes')
    def bodaabejorros_listarAsistentes(self,request):
        mcr = AsistenteCollectionResponse()
        qry = Asistente.query()
        for q in qry:
            f = q.fecha.strftime("%Y-%m-%d %H:%M:%S")
            mensajeRecibido = AsistenteResponse(email=q.email,nombre=q.nombre,fecha=f,mensaje=q.mensaje,
                requerimientos=q.requerimientos,eventos=q.eventos)
            mcr.items.append(mensajeRecibido)
        return mcr

    #Defino el recurso asistente
    ASISTENTE_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        nombre=messages.StringField(2,variant=messages.Variant.STRING),
        email=messages.StringField(3,variant=messages.Variant.STRING),
        mensaje=messages.StringField(4,variant=messages.Variant.STRING),
        requerimientos=messages.StringField(5,variant=messages.Variant.STRING),
        eventos=messages.StringField(6,variant=messages.Variant.STRING))

    #guardar un asistente
    @endpoints.method(ASISTENTE_RESOURCE, AsistenteCollectionResponse,
        path='guardarAsistente', http_method='POST', name='bodaabejorros.guardarAsistente')
    def bodaabejorros_guardarAsistente(self,request):
        msg = Asistente(email=request.email,nombre=request.nombre,
            mensaje=request.mensaje,requerimientos=request.requerimientos,eventos=request.eventos)
        msg.put()
        f = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mcr = AsistenteCollectionResponse()
        mcr.items.append(AsistenteResponse(email=request.email,nombre=request.nombre,
            fecha=f,mensaje=request.mensaje,requerimientos=request.requerimientos,eventos=request.eventos))
        qry = Asistente.query()
        for q in qry:
            f = q.fecha.strftime("%Y-%m-%d %H:%M:%S")
            mensajeRecibido = AsistenteResponse(email=q.email,nombre=q.nombre,fecha=f,mensaje=q.mensaje,
                requerimientos=q.requerimientos,eventos=q.eventos)
            mcr.items.append(mensajeRecibido)
        return mcr

    #listar todas las fotos
    @endpoints.method(message_types.VoidMessage, FotoCollectionResponse,
        path='listarFotos', http_method='GET', name='bodaabejorros.listarFotos')
    def bodaabejorros_listarFotos(self,request):
        mcr = FotoCollectionResponse()
        qry = Foto.query()
        for q in qry:
            f = q.fecha.strftime("%Y-%m-%d %H:%M:%S")
            mensajeRecibido = FotoResponse(categoria=q.categoria,titulo=q.titulo,fecha=f,
                descripcion=q.descripcion,url=q.url)
            mcr.items.append(mensajeRecibido)
        return mcr

    #Defino el recurso foto
    FOTO_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        categoria=messages.StringField(2,variant=messages.Variant.STRING),
        titulo=messages.StringField(3,variant=messages.Variant.STRING),
        descripcion=messages.StringField(4,variant=messages.Variant.STRING),
        url=messages.StringField(5,variant=messages.Variant.STRING))

    #guardar una foto
    @endpoints.method(FOTO_RESOURCE, FotoCollectionResponse,
        path='guardarFotos', http_method='POST', name='bodaabejorros.guardarFotos')
    def boda_abejorros_guardarFotos(self,request):
        msg = Foto(categoria=request.categoria,titulo=request.titulo,
                descripcion=request.descripcion,url=request.url)
        msg.put()
        f = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mcr = FotoCollectionResponse()
        mcr.items.append(FotoResponse(categoria=request.categoria,titulo=request.titulo,fecha=f,
                descripcion=request.descripcion,url=request.url))
        qry = Foto.query()
        for q in qry:
            f = q.fecha.strftime("%Y-%m-%d %H:%M:%S")
            mensajeRecibido = FotoResponse(categoria=q.categoria,titulo=q.titulo,fecha=f,
                descripcion=q.descripcion,url=q.url)
            mcr.items.append(mensajeRecibido)
        return mcr


APPLICATION = endpoints.api_server([BodaAbejorrosAPI])
