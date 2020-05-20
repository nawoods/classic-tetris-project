from django.contrib import admin

from ..models import User, DiscordUser, TwitchUser, WebsiteUser, Match, Game, TwitchChannel, CustomCommand


class DiscordUserInline(admin.StackedInline):
    model = DiscordUser

class TwitchUserInline(admin.StackedInline):
    model = TwitchUser

class WebsiteUserInline(admin.StackedInline):
    model = WebsiteUser

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [DiscordUserInline, TwitchUserInline, WebsiteUserInline]

@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    list_display = ("username", "discriminator", "discord_id")

admin.site.register(TwitchUser)


class GameInline(admin.TabularInline):
    model = Game

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    inlines = [GameInline]
    list_display = ('__str__', 'player1', 'wins1', 'player2', 'wins2', 'channel', 'ended_at')


class CustomCommandInline(admin.TabularInline):
    model = CustomCommand

@admin.register(TwitchChannel)
class TwitchChannelAdmin(admin.ModelAdmin):
    inlines = [CustomCommandInline]
    list_display = ("__str__", "twitch_user", "connected")
