# Generated by Django 3.1.5 on 2021-02-24 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acapp', '0002_auto_20210205_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id_card',
            field=models.CharField(max_length=12, verbose_name='身分證字號'),
        ),
        migrations.AlterField(
            model_name='member',
            name='job_title',
            field=models.CharField(max_length=100, verbose_name='職稱'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='手機號碼'),
        ),
        migrations.CreateModel(
            name='postBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255, verbose_name='標題名稱')),
                ('blog_content', models.TextField(blank=True, verbose_name='標題內容')),
                ('photo', models.ImageField(upload_to='image/')),
                ('blog_created_at', models.DateTimeField(auto_now=True)),
                ('authBlogId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acapp.member', verbose_name='隸屬身份')),
            ],
        ),
    ]
