from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def forwards_func(apps, schema_editor):
    Tournament = apps.get_model('base', 'Tournament')
    Match = apps.get_model('base', 'Match')
    db_alias = schema_editor.connection.alias

    for klass in (Tournament, Match):
        instances = klass.objects.using(db_alias).all()
        for instance in instances:
            player = getattr(instance, 'created_by')
            user = getattr(player, 'user')
            setattr(instance, 'created_by_user', user)

        klass.objects.using(db_alias).bulk_update(instances, ['created_by_user'])


def reverse_func(apps, schema_editor):
    Tournament = apps.get_model('base', 'Tournament')
    Match = apps.get_model('base', 'Match')
    PlayerProfile = apps.get_model('base', 'PlayerProfile')
    db_alias = schema_editor.connection.alias

    for klass in (Tournament, Match):
        instances = klass.objects.using(db_alias).all()
        for instance in instances:
            user = getattr(instance, 'created_by_user')
            player = PlayerProfile.objects.using(db_alias).filter(user=user).first()
            setattr(instance, 'created_by', player)

        klass.objects.using(db_alias).bulk_update(instances, ['created_by'])


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_auto_20200605_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PlayerProfile', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PlayerProfile', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='created_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='created_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
        migrations.RunPython(forwards_func, reverse_func),
        migrations.RemoveField(
            model_name='tournament',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='match',
            name='created_by',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='created_by_user',
            new_name='created_by'
        ),
        migrations.RenameField(
            model_name='match',
            old_name='created_by_user',
            new_name='created_by'
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)
        ),
        migrations.AlterField(
            model_name='match',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)
        )
    ]
