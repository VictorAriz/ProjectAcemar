from rest_framework.serializers import ModelSerializer
from apps.users.models import Profile
from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from apps.users.models import ED_kindId, ED_userState
from apps.serviceProvider.models import ED_service_provider
from apps.serviceProvider.serializers import serviceProviderRegistrationSerializer
from django.contrib.auth.models import User
import base64,os


class profileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        #fields = ('name', 'pk')
        fields = ('__all__')

class profileRegisterSerializer(ModelSerializer):
    serviceProvider = serviceProviderRegistrationSerializer(many=False)
    class Meta:
        model = Profile
        fields = ('phone', 'nationalId', 'description', 'isProvider', 'profileImage', 'idImage', 'kindId', 'deviceId', 'serviceProvider', 'userState')

        # fields = ('__all__')
    # def create(self, validated_data):
    #     provider_data = validated_data.pop('serviceProvider')
    #     profile = profile.objects.create(**validated_data)
    #     ED_service_provider.objects.create(profile=profile, **provider_data)
    #     return profile


class userSerializer(ModelSerializer):
    profile = profileSerializer(many = False)
    class Meta:
        model = User
        #fields = ('name', 'pk')
        fields = ('__all__')

class userRegisterSerializer(ModelSerializer):
    profile = profileRegisterSerializer(many = False)
    class Meta:
        model = User
        #fields = ('name', 'pk')
        fields = ('__all__')
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        # provider_data = validated_data.pop('profile')
        servicePr = ED_service_provider.objects.create(**profile_data)
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, ServiceProvider=servicePr, **profile_data)
        return user



class RegisterSerializer(serializers.Serializer):
  #class Meta:
  	#fields = ('__all__')
  	#extra_kwargs = {"username": {"error_messages": {"required": "Give yourself a username"}}}
  #	error_messages = {"username": {"required": "For some reason this is a custom error message overriding the model default"}}
  #def __init__(self, *args, **kwargs):
  #	super(serializers.Serializer, self).__init__(*args, **kwargs)
  #	self.fields['username'].error_messages['required'] = u'My custom required msg'
  username = serializers.CharField(required=True)
  email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
  password1 = serializers.CharField(required=True)
  password2 = serializers.CharField(required=True)
  first_name = serializers.CharField(required=True)
  nationalId = serializers.CharField(required=False)
  description = serializers.CharField(required = False)
  isProvider = serializers.IntegerField(required=True)
  kindId = serializers.IntegerField(required = False)
  profileImage = serializers.ImageField(required = False)
  idImage = serializers.FileField(required = False)
  phone = serializers.CharField(required = False)
  idServiceType = serializers.IntegerField(required = False)
  
  def validate_password1(self, password):
    return get_adapter().clean_password(password)

  def validate(self, data):
    if data['password1'] != data['password2']:
        raise serializers.ValidationError(
            ("Los dos password no son iguales."))
    if User.objects.filter(username = data['username']).exists():
    	raise serializers.ValidationError(("El usuario ya esta registrado."))
    print(str(data))
    return data
  
  def validate_email(self, email):
    email = get_adapter().clean_email(email)
    if allauth_settings.UNIQUE_EMAIL:
      if email and email_address_exists(email):
        raise serializers.ValidationError(
            ("El email ya esta registrado."))
    return email

  def validate_usernamee(self, data):
  	username = data['username']
  	if User.objects.filter(username=username).exists():
  		raise serializers.ValidationError(
            ("El usuario ya esta registrado."))
  	return data

  def get_cleaned_data(self):
      return {
          'username': self.validated_data.get('username', ''),
          'email': self.validated_data.get('email', ''),
          'password1': self.validated_data.get('password1', ''),
          'password2': self.validated_data.get('password2', ''),
          'first_name': self.validated_data.get('first_name', ''),
          'isProvider': self.validated_data.get('isProvider', ''),
          'description': self.validated_data.get('description', ''),
          'phone': self.validated_data.get('phone', ''),
          'nationalId': self.validated_data.get('nationalId', ''),
          'kindId': self.validated_data.get('kindId', ''),
          'profileImage': self.validated_data.get('profileImage',''),
          'idImage': self.validated_data.get('idImage', ''),
          'idServiceType': self.validated_data.get('idServiceType', ''),
      }
      
  def save(self, request):
      adapter = get_adapter()
      user = adapter.new_user(request)
      self.cleaned_data = self.get_cleaned_data()
      adapter.save_user(request, user, self)
      #print(request.data["kindId"])
      setup_user_email(request, user, [])
      user.profile.phone = request.data["phone"]
      profile = user.profile
      profile.isProvider = request.data['isProvider']
      if request.data["isProvider"] == "1":
        user.groups.add(2)
        profile.userState = ED_userState.objects.get(id = 1)
        print ("--------------------------------")
        if 'profileImage' in request.data:
            profile.profileImage = request.data["profileImage"]
            image = request.data["profileImage"]
        else:
            profile.profileImage = ''
            image = ''
        profile.kindId = ED_kindId.objects.get(id=request.data["kindId"])
        profile.description = request.data['description']
        profile.idImage = request.data["idImage"]
        idServiceType = request.data['idServiceType']
        user.profile.nationalId = request.data["nationalId"]
        provider = ED_service_provider.objects.create(name = request.data["first_name"], description = request.data['description'], email = request.data['email'], phone = request.data['phone'], nationalId = request.data['nationalId'], photo = image, file = request.data['idImage'])
        profile.serviceProvider = provider
        profile.save()
      else:
        user.groups.add(1)
        profile.userState = ED_userState.objects.get(id = 2)
        profile.save()
      user.profile.save()
      return user

 