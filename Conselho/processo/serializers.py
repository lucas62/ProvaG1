from rest_framework import routers, serializers, viewsets
from processo.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'is_staff')

    def create(self, validated_data):
       return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.is_staff = validated_data.get('is_staff',instance.is_staff)
        instace.save()
        return instace

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleicao
        fields = '__all__'

   def create(self, validated_data):
       return Eleicao.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.tipo = validated_data.get('nome',instance.nome)
        instance.data_Inicio = validated_data.get('data_Inicio',instance.data_Inicio)
        instance.data_Fim = validated_data.get('data_Fim',instance.data_Fim)
        instance.local = validated_data.get('local',instance.local)
        instace.save()
        return instace

class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    token = TokenSerializer(many=False)
    class Meta:
        model = Eleitor
        fields = '__all__'

    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        eleitor = Eleitor.objects.create(**validated_data,user = user)
        return eleitor

    def update(self,instance,validated_data):
        instance.nome = validated_data.get('nome',instance.nome)
        instance.cpf = validated_data.get('cpf',instance.cpf)
        instance.user = validated_data.get('user',instance.user)
        instace.token = validated_data.get('token',instace.token)
        instace.save()
        return instace

class VagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'

    def create(self, validated_data):
       return Vaga.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.nome = validated_data.get('nome',instance.nome)
        instance.descricao = validated_data.get('descricao',instance.descricao)
        instace.save()
        return instace

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    vaga = VagaSerializer(many=False)
    class Meta:
        model = Candidato
        fields = '__all__'

    def create(self, validated_data):
       return Candidato.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.nome = validated_data.get('nome',instance.nome)
        instance.cpf = validated_data.get('cpf',instance.cpf)
        instance.rg = validated_data.get('rg',instance.rg)
        instance.codigo_Candidatura = validated_data.get('codigo_Candidatura',instance.codigo_Candidatura)
        instace.vaga = validated_data.get('vaga',instace.vaga)
        instace.save()
        return instace

class VotoSerializer(serializers.HyperlinkedModelSerializer):
    eleicao = EleicaoSerializer(many=False)
    candidato = CandidatoSerializer(many=False)
    class Meta:
        model = Voto
        fields = '__all__'

    def create(self, validated_data):
       return Voto.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.voto = validated_data.get('voto',instance.voto)
        instance.eleicao = validated_data.get('eleicao',instance.eleicao)
        instance.candidato = validated_data.get('candidato',instance.candidato)
        instance.data_Voto = validated_data.get('data_Voto',instance.data_Voto)
        instace.save()
        return instace

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resultado
        fields = '__all__'