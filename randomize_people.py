import json
import random

from Person import Person

MAX_TREASURER_COUNT = 6

saved_data = {
  'people': [
    {
      'name': 'fox',
      'is_treasurer': True,
      'history': {}
    },
    {
      'name': 'falco',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'marth',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'sheik',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'peach',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'puff',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'captain falcon',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'popo',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'nana',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'samus',
      'is_treasurer': True,
      'history': {}
    },
    {
      'name': 'link',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'mario',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'isabelle',
      'is_treasurer': False,
      'history': {}
    },
    {
      'name': 'waluigi',
      'is_treasurer': True,
      'history': {}
    },
  ]
}

if __name__ == '__main__':
  treasurers = []
  non_treasurers = []

  people = []
  json_data = open('data.json').read()
  people_data = json.loads(json_data)

  for json_person in people_data['people']:
    people.append(Person(json_person['name'], json_person['history'], json_person['is_treasurer']))

  for person in people:
    if person.is_treasurer and len(treasurers) <= MAX_TREASURER_COUNT:
      treasurers.append(person)
    else:
      non_treasurers.append(person)

  groups = {}
  for index, treasurer in enumerate(treasurers):
    groups[index] = {
      'treasurer': treasurer,
      'members': []
    }

  keep_generating_groups = True
  while keep_generating_groups: 
    random.shuffle(non_treasurers)
    for index, person in enumerate(non_treasurers):
      groups[index%3]['members'].append(person)

    group_member_names = []
    for group_number in groups:
      group = groups[group_number]
      group_members = [group['treasurer']] + group['members']
      group_names = [member.name for member in group_members]
      group_member_names.append(group_names)
      for member in group_members:
        for name in group_names:
          if not name == member.name:
            member.add_history(name)
          json_member = [json_entry for json_entry in people_data['people'] if json_entry['name'] == name][0]
          json_member['history'] = member.history
    
    print group_member_names
    should_continue = raw_input('Keep this configuration? (y/N)')
    if should_continue == 'y':
      keep_generating_groups = False
    else:
      for group_number in groups:
        group = groups[group_number]
        group['members'] = []


  with open('data.json', 'w') as outfile:
    json.dump(people_data, outfile)