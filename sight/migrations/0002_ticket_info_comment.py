# Generated by Django 4.0 on 2022-08-11 01:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('sight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('desc', models.CharField(blank=True, max_length=64, null=True, verbose_name='描述')),
                ('types', models.SmallIntegerField(choices=[(11, '成人票'), (12, '儿童票')], default=11, help_text='默认为成人票', verbose_name='类型')),
                ('price', models.FloatField(verbose_name='价格（原价）')),
                ('discount', models.FloatField(default=10, verbose_name='折扣')),
                ('total_stock', models.PositiveIntegerField(default=0, verbose_name='总库存')),
                ('remain_stock', models.PositiveIntegerField(default=0, verbose_name='剩余库存')),
                ('expire_date', models.IntegerField(default=1, verbose_name='有效期')),
                ('return_policy', models.CharField(default='条件退', max_length=64, verbose_name='退改政策')),
                ('has_invoice', models.BooleanField(default=True, verbose_name='是否提供发票')),
                ('entry_way', models.SmallIntegerField(choices=[(0, '短信换票入园'), (1, '凭借验证码入园')], default=0, verbose_name='入园方式')),
                ('tips', models.TextField(blank=True, null=True, verbose_name='预定须知')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='其他说明')),
                ('status', models.SmallIntegerField(choices=[(1, '开放购买'), (0, '暂未开放')], default=1, verbose_name='状态')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to='sight.sight', verbose_name='景点门票')),
            ],
            options={
                'db_table': 'sight_ticket',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_explain', models.CharField(blank=True, max_length=1024, null=True, verbose_name='入园参考')),
                ('play_way', models.TextField(blank=True, null=True, verbose_name='特色玩法')),
                ('tips', models.TextField(blank=True, null=True, verbose_name='温馨提示')),
                ('traffic', models.TextField(blank=True, null=True, verbose_name='交通到达')),
                ('sight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sight.sight')),
            ],
            options={
                'db_table': 'sight_info',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('content', models.TextField(blank=True, null=True, verbose_name='评论内容')),
                ('is_top', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('love_count', models.IntegerField(default=0, verbose_name='点赞次数')),
                ('score', models.FloatField(default=5, verbose_name='评分')),
                ('ip_address', models.CharField(blank=True, max_length=64, null=True, verbose_name='IP地址')),
                ('is_public', models.SmallIntegerField(default=1, verbose_name='是否公开')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment', to='sight.comment', verbose_name='回复')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sight.sight', verbose_name='景点')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.user', verbose_name='评论人')),
            ],
            options={
                'db_table': 'sight_comment',
                'ordering': ['-love_count', '-created_at'],
            },
        ),
    ]
