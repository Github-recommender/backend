import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()
    lol = graphene.Int()

    def resolve_hello(self, args, info):
        return 'World'

    def resolve_lol(self,args, info):
        return 2

class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, args, info):
        return '{} {}'.format(self.first_name, self.last_name)

class CreatePerson(graphene.Mutation):
    class Input:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field('Person')

    @classmethod
    def mutate(cls, instance, args, info):
        person = Person(name=args.get('name'))
        ok = True
        return CreatePerson(person=person, ok=ok)

class Person(graphene.ObjectType):
    name = graphene.String()

class MyMutations(graphene.ObjectType):
    create_person = graphene.Field(CreatePerson)

schema = graphene.Schema()


schema = graphene.Schema(query=Query, mutation=MyMutations)
