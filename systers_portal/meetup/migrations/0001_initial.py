# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-08 17:45
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('users', '0001_squashed_0003_auto_20160207_1550'),
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('date', models.DateField(verbose_name='Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date')),
                ('time', models.TimeField(blank=True, verbose_name='Time')),
                ('end_time', models.TimeField(null=True, verbose_name='End Time')),
                ('venue', models.CharField(blank=True, max_length=512, verbose_name='Venue')),
                ('description', models.TextField(verbose_name='Description')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SystersUser', verbose_name='Created By')),
            ],
        ),
        migrations.CreateModel(
            name='MeetupLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('sponsors', ckeditor.fields.RichTextField(blank=True, verbose_name='Sponsors')),
                ('join_requests', models.ManyToManyField(blank=True, related_name='Join_Requests', to='users.SystersUser', verbose_name='Join Requests')),
                ('leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_leader', to='users.SystersUser', verbose_name='Community leader')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Location')),
                ('members', models.ManyToManyField(blank=True, related_name='community_members', to='users.SystersUser', verbose_name='Community Members')),
                ('moderators', models.ManyToManyField(related_name='community_moderators', to='users.SystersUser', verbose_name='Community Moderators')),
            ],
            options={
                'permissions': (('add_meetup_location_member', 'Add meetup location member'), ('delete_meetup_location_member', 'Delete meetup location member'), ('add_meetup_location_moderator', 'Add meetup location moderator'), ('delete_meetup_location_moderator', 'Delete meetup location moderator'), ('approve_meetup_location_joinrequest', 'Approve meetup location join request'), ('reject_meetup_location_joinrequest', 'Reject meetup location join request'), ('approve_meetup_location_meetuprequest', 'Approve meetup location meetup request'), ('reject_meetup_location_meetuprequest', 'Reject meetup location meetup request'), ('view_meetup_location_meetuprequest', 'View meetup location meetup request'), ('approve_meetup_comment', 'Approve comment for a meetup'), ('reject_meetup_comment', 'Reject comment for a meetup'), ('add_meetup_rsvp', 'RSVP for a meetup'), ('approve_support_request', 'Approve support request'), ('reject_support_request', 'Reject support request'), ('add_support_request_comment', 'Add comment for a support request'), ('edit_support_request_comment', 'Edit comment for a support request'), ('delete_support_request_comment', 'Delete comment for a support request'), ('approve_support_request_comment', 'Approve comment for a support request'), ('reject_support_request_comment', 'Reject comment for a support request')),
            },
        ),
        migrations.CreateModel(
            name='RequestMeetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(blank=True, verbose_name='Time')),
                ('venue', models.CharField(blank=True, max_length=512, verbose_name='Venue')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approvedBy', to='users.SystersUser')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SystersUser', verbose_name='Created By')),
                ('meetup_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetup.MeetupLocation', verbose_name='Meetup Location')),
            ],
        ),
        migrations.CreateModel(
            name='RequestMeetupLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name of the Meetup Location.(Naming convention for Systers meetup location is City+Systers.e.g.London Systers, Boston Systers.)')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug of the Meetup Location')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description of the Meetup Location')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email of the Meetup Location if any.')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Is this Approved?')),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approvedby', to='users.SystersUser', verbose_name='Approved By')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdby', to='users.SystersUser', verbose_name='Requested By')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coming', models.BooleanField(default=True)),
                ('plus_one', models.BooleanField(default=False)),
                ('meetup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetup.Meetup', verbose_name='Meetup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.SystersUser', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='SupportRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('is_approved', models.BooleanField(default=False)),
                ('meetup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetup.Meetup', verbose_name='Meetup')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.SystersUser', verbose_name='Volunteer')),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='meetup_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetup.MeetupLocation', verbose_name='Meetup Location'),
        ),
        migrations.AlterUniqueTogether(
            name='rsvp',
            unique_together=set([('user', 'meetup')]),
        ),
    ]
