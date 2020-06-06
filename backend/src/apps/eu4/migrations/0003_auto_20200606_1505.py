from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


def forwards_func(apps, schema_editor):
    Tournament = apps.get_model('eu4', 'EU4Tournament')
    Match = apps.get_model('eu4', 'EU4Match')
    db_alias = schema_editor.connection.alias

    for klass in (Tournament, Match):
        instances = klass.objects.using(db_alias).all()
        for instance in instances:
            player_id = getattr(instance, 'created_by')
            user = getattr(player_id, 'user')
            setattr(instance, 'created_by_user', user)

        klass.objects.using(db_alias).bulk_update(instances, ['created_by_user'])


def reverse_func(apps, schema_editor):
    Tournament = apps.get_model('eu4', 'EU4Tournament')
    Match = apps.get_model('eu4', 'EU4Match')
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
        ('eu4', '0002_auto_20200605_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eu4tournament',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PlayerProfile', null=True,
                                    blank=True),
        ),
        migrations.AlterField(
            model_name='eu4match',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PlayerProfile', null=True,
                                    blank=True),
        ),
        migrations.AddField(
            model_name='eu4match',
            name='created_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL,
                                    blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eu4tournament',
            name='created_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL,
                                    blank=True, null=True),
        ),
        migrations.RunPython(forwards_func, reverse_func),
        migrations.RemoveField(
            model_name='eu4tournament',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='eu4match',
            name='created_by',
        ),
        migrations.RenameField(
            model_name='eu4tournament',
            old_name='created_by_user',
            new_name='created_by'
        ),
        migrations.RenameField(
            model_name='eu4match',
            old_name='created_by_user',
            new_name='created_by'
        ),
        migrations.AlterField(
            model_name='eu4tournament',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)
        ),
        migrations.AlterField(
            model_name='eu4match',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)
        ),
        migrations.AlterField(
            model_name='eu4tournament',
            name='schedule',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
