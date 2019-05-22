from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, usuario, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not usuario:
            raise ValueError('The given username must be set')
        usuario = self.model.normalize_username(usuario)
        user = self.model(usuario=usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(usuario, password, **extra_fields)

    def create_superuser(self, usuario, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(usuario, password, **extra_fields)


class Role(models.Model):

    """
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    """
    STUDENT = 1
    TEACHER = 2
    SECRETARY = 3
    SUPERVISOR = 4
    ADMIN = 5
    ROLE_CHOICES = (
        (STUDENT, "dsaasd"),
        (TEACHER, "asdasd"),
        (SECRETARY, "dasdasd"),
        (SUPERVISOR, "dsasdas"),
        (ADMIN, "dsadasd"),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    # def __str__(self):
    #     return self.get_id_display()


class User(AbstractBaseUser, PermissionsMixin):

    MEDICO = "is_medico"
    ENFERMAGEM = "is_enfermagem"
    FARMACIA = "is_farmacia"
    PACIENTE = "is_paciente"
    ADMIN = "is_admin"

    ROLE_CHOICES = (
        (MEDICO, "Médico"),
        (ENFERMAGEM, "Enfermagem"),
        (FARMACIA, "Farmácia"),
        (PACIENTE, "Paciente"),
        (ADMIN, "Admin"),
    )
    usuario = models.CharField('Usuário', max_length=14, unique=True)
    nome = models.CharField('Nome de Usuário', max_length=80, blank=True)
    nome_mae = models.CharField('Nome da mãe', max_length=80, null=True, blank=True)
    credencial = models.CharField('Número do Conselho', max_length=10, blank=True)
    roles = models.CharField('Tipo', max_length=15, choices=ROLE_CHOICES, default=MEDICO)
    is_active = models.BooleanField('Ativo', blank=True, default=True)
    is_staff = models.BooleanField('Equipe', blank=True, default=False)
    date_joined = models.DateTimeField('Criado em', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.usuario

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
