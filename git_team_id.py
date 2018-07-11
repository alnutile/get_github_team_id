from github import Github
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('token', action="store")
parser.add_argument('org', action="store")
parser.add_argument('team_name', action="store")
args = parser.parse_args()
# Github Enterprise with custom hostname
g = Github(args.token)

# Then play with your Github objects:
for team in g.get_organization(args.org).get_teams():
    if team.name == args.team_name:
        print("{} has id {}".format(team.name, team.id))


print("Done looking over teams")
