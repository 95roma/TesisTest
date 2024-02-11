# Generated by Django 3.0.6 on 2023-12-22 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DireccionApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=9)),
                ('TelefonoDos', models.CharField(max_length=9)),
                ('Departamento', models.CharField(max_length=20)),
                ('Municipio', models.CharField(max_length=30)),
                ('Distrito', models.CharField(max_length=20)),
                ('Estado', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Agencia',
                'verbose_name_plural': 'Agencias',
                'db_table': 'Agencia',
            },
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Alternativa', models.CharField(max_length=100)),
                ('MontoMini', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MontoMaxi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Plazo', models.IntegerField()),
                ('PlazoMese', models.IntegerField()),
                ('Estado', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Alternativa',
                'verbose_name_plural': 'Alternativas',
                'db_table': 'Alternativa',
            },
        ),
        migrations.CreateModel(
            name='DocumentosClie',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateTimeField(auto_now=True)),
                ('Archivo', models.FileField(upload_to='documentos/')),
                ('NombreDocu', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'DocumentosClie',
                'verbose_name_plural': 'DocumentosClies',
                'db_table': 'DocumentosClie',
            },
        ),
        migrations.CreateModel(
            name='Infraestructura',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Tipo', models.CharField(max_length=100)),
                ('TipoLoteMej', models.CharField(max_length=10)),
                ('Estado', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Infraestructura',
                'verbose_name_plural': 'Infraestructuras',
                'db_table': 'Infraestructura',
            },
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Unidad', models.CharField(max_length=10)),
                ('Estado', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Materiales',
                'verbose_name_plural': 'Materialess',
                'db_table': 'Materiales',
            },
        ),
        migrations.CreateModel(
            name='ModeloVivi',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TipoVivi', models.CharField(max_length=200)),
                ('Modelo', models.FileField(upload_to='documentos/')),
                ('MontoCons', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Descripcion', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'ModeloVivi',
                'verbose_name_plural': 'ModeloVivis',
                'db_table': 'ModeloVivi',
            },
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Estado', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Ocupacion',
                'verbose_name_plural': 'Ocupacions',
                'db_table': 'Ocupacion',
            },
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TipoSala', models.CharField(max_length=100)),
                ('SalarioMaxi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('SalarioMini', models.DecimalField(decimal_places=2, max_digits=10)),
                ('FechaInic', models.DateField()),
                ('FechaFina', models.DateField(blank=True, null=True)),
                ('Estado', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Salario',
                'verbose_name_plural': 'Salarios',
                'db_table': 'Salario',
            },
        ),
        migrations.CreateModel(
            name='SolicitudInscSegEnf',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('NombreEnfe', models.CharField(max_length=50)),
                ('Estado', models.CharField(max_length=10)),
                ('Personal', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'SolicitudInscSegEnf',
                'verbose_name_plural': 'SolicitudInscSegEnfs',
                'db_table': 'SolicitudInscSegEnf',
            },
        ),
        migrations.CreateModel(
            name='TasaInte',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('NumeroCred', models.CharField(max_length=60)),
                ('Interes', models.IntegerField()),
                ('Estado', models.IntegerField()),
            ],
            options={
                'verbose_name': 'TasaInte',
                'verbose_name_plural': 'TasaInte',
                'db_table': 'TasaInte',
            },
        ),
        migrations.CreateModel(
            name='TipoOper',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'TipoOper',
                'verbose_name_plural': 'TipoOpers',
                'db_table': 'TipoOper',
            },
        ),
        migrations.CreateModel(
            name='ZonaAgen',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('NombreZona', models.CharField(max_length=60)),
                ('IdAgencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfiguracionApp.Agencia')),
            ],
            options={
                'verbose_name': 'ZonaAgen',
                'verbose_name_plural': 'ZonaAgens',
                'db_table': 'ZonaAgen',
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('IdDistrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DireccionApp.Distrito')),
                ('IdZonaAgen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfiguracionApp.ZonaAgen')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'db_table': 'Zona',
            },
        ),
        migrations.CreateModel(
            name='RangoFina',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('VecesFina', models.DecimalField(decimal_places=2, max_digits=5)),
                ('MontoMini', models.DecimalField(decimal_places=2, max_digits=8)),
                ('MontoMaxi', models.DecimalField(decimal_places=2, max_digits=8)),
                ('IdAlternativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfiguracionApp.Alternativa')),
                ('IdSalario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfiguracionApp.Salario')),
            ],
            options={
                'verbose_name': 'RangoFina',
                'verbose_name_plural': 'RangoFina',
                'db_table': 'RangoFina',
            },
        ),
    ]
