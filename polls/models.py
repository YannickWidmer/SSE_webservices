# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Attribute(models.Model):
    player_character = models.ForeignKey('PlayerCharacter', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute'
        unique_together = (('player_character', 'name'),)


class Clothe(models.Model):
    item_id = models.ForeignKey('Item', models.DO_NOTHING, primary_key=True)
    wheater_protection = models.IntegerField()
    protection = models.IntegerField()
    bodypart = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'clothe'


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    gcm_token = models.CharField(max_length=255, blank=True, null=True)
    last_connected = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'device'


class Foe(models.Model):
    foe_archetyp_id = models.IntegerField()
    foe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    stamina_reserve_max = models.IntegerField(blank=True, null=True)
    stamina_reserve_now = models.IntegerField(blank=True, null=True)
    stamina_available_now = models.IntegerField(blank=True, null=True)
    stamina_available_used = models.IntegerField(blank=True, null=True)
    stamina_available_max = models.IntegerField(blank=True, null=True)
    stamina_available_recover = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foe'


class FoeArchetyp(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    foe_archetyp = models.ForeignKey('Relationable', models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey('FoeGroup', models.DO_NOTHING)
    actions = models.TextField()
    name = models.CharField(max_length=255, blank=True, null=True)
    max_health = models.IntegerField(blank=True, null=True)
    max_stamina = models.IntegerField(blank=True, null=True)
    max_stamina_available = models.IntegerField(blank=True, null=True)
    stamina_recover = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foe_archetyp'


class FoeGroup(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    foe_group = models.ForeignKey('Relationable', models.DO_NOTHING, primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foe_group'


class Item(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    item_id = models.ForeignKey('Relationable', models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey('ItemGroup', models.DO_NOTHING, blank=True, null=True)
    archetyp_id = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    contained_in = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='item_contained_in')
    name = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    weight_unit = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    value_unit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class ItemContainer(models.Model):
    item_id = models.ForeignKey(Item, models.DO_NOTHING, primary_key=True)
    config = models.TextField()

    class Meta:
        managed = False
        db_table = 'item_container'


class ItemGroup(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    item_group = models.ForeignKey('Relationable', models.DO_NOTHING, primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_group'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Npc(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    npc = models.ForeignKey('Relationable', models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey('NpcGroup', models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'npc'


class NpcGroup(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    npc_group = models.ForeignKey('Relationable', models.DO_NOTHING, primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'npc_group'


class Place(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    place_id = models.ForeignKey('Relationable', models.DO_NOTHING, primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=32, blank=True, null=True)
    icon_url = models.CharField(max_length=255, blank=True, null=True)
    placement_in_parent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place'


class PlayerCharacter(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    player_character = models.ForeignKey('Relationable', models.DO_NOTHING, primary_key=True)
    belongsto = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    race = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    background = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_character'


class Relation(models.Model):
    from_field = models.ForeignKey('Relationable', models.DO_NOTHING, db_column='from_id', related_name='relation_from_field')  # Field renamed because it was a Python reserved word.
    to = models.ForeignKey('Relationable', models.DO_NOTHING)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'relation'


class Relationable(models.Model):
    relationable_id = models.AutoField(primary_key=True)
    world = models.ForeignKey('World', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'relationable'


class Scenario(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    scenario_id = models.ForeignKey(Relationable, models.DO_NOTHING, primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario'


class ScenarioOrder(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    from_field = models.ForeignKey(Scenario, models.DO_NOTHING, db_column='from_id', related_name='ScenarioOrder_from_field')  # Field renamed because it was a Python reserved word.
    to = models.ForeignKey(Scenario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scenario_order'
        unique_together = (('from_field', 'to'),)


class Spell(models.Model):
    usable = models.ForeignKey('Usable', models.DO_NOTHING, primary_key=True)
    mana_needed = models.IntegerField()
    mana_max = models.IntegerField()
    mana_used = models.IntegerField()
    difficulty = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spell'


class State(models.Model):
    player_character = models.ForeignKey(PlayerCharacter, models.DO_NOTHING, primary_key=True)
    life_max = models.IntegerField(blank=True, null=True)
    life_now = models.IntegerField(blank=True, null=True)
    stamina_reserve_max = models.IntegerField(blank=True, null=True)
    stamina_reserve_now = models.IntegerField(blank=True, null=True)
    stamina_available_max = models.IntegerField(blank=True, null=True)
    stamina_available_now = models.IntegerField(blank=True, null=True)
    stamina_available_used = models.IntegerField(blank=True, null=True)
    mentalstate_x = models.IntegerField(blank=True, null=True)
    mentalstate_y = models.IntegerField(blank=True, null=True)
    mentalstate = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class Story(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    story_id = models.ForeignKey(Relationable, models.DO_NOTHING, primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story'


class Talent(models.Model):
    player_character = models.ForeignKey(PlayerCharacter, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talent'
        unique_together = (('player_character', 'name'),)


class Usable(models.Model):
    item_id = models.ForeignKey(Item, models.DO_NOTHING, primary_key=True)
    actions = models.TextField()
    usable_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'usable'


class UsableState(models.Model):
    usable = models.ForeignKey(Usable, models.DO_NOTHING)
    state = models.ForeignKey(State, models.DO_NOTHING)
    mana_needed = models.IntegerField()
    mana_max = models.IntegerField()
    mana_used = models.IntegerField()
    difficulty = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usable_state'
        unique_together = (('usable', 'state'),)


class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, models.DO_NOTHING, blank=True, null=True)
    phpsess_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_info'


class UserWorldRole(models.Model):
    world = models.ForeignKey('World', models.DO_NOTHING)
    user = models.ForeignKey(UserInfo, models.DO_NOTHING)
    role = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_world_role'
        unique_together = (('user', 'world'),)


class World(models.Model):
    world_id = models.AutoField(primary_key=True)
    world_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world'
