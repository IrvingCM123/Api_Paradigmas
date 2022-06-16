import graphene
from graphene_django import DjangoObjectType

from .models import Topdiez


class TopdiezType(DjangoObjectType):
    class Meta:
        model = Topdiez


class Query(graphene.ObjectType):
    topdiez = graphene.List(TopdiezType)

    def resolve_topdiez(self, info, **kwargs):
        return Topdiez.objects.all()


class CreateTopdiez(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    genero = graphene.String()
    description = graphene.String()
    capitulos = graphene.String()
    duracion = graphene.String()
    temporadas = graphene.String()
    fecha = graphene.String()
    
    
    class Arguments:
        nombre = graphene.String()
        genero = graphene.String()
        description = graphene.String()
        capitulos = graphene.String()
        duracion = graphene.String()
        temporadas = graphene.String()
        fecha = graphene.String()

    
    def mutate(self, info, nombre, genero, description, capitulos, duracion, temporadas, fecha):
        top = Topdiez(nombre=nombre, genero = genero, description=description, capitulos = capitulos, duracion = duracion, temporadas = temporadas, fecha = fecha )
        top.save()

        return CreateTopdiez(
            id=top.id,
            nombre=top.nombre,
	    genero=top.genero,
            description=top.description,
	    capitulos=top.capitulos,
	    duracion=top.duracion,
	    temporadas=top.temporadas,
	    fecha=top.fecha,
        )



class Mutation(graphene.ObjectType):
    create_top = CreateTopdiez.Field()
