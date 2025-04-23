# Create a dictionary of your profile and print it nicely

profile = {
    "Himanshu": {"name": "Himanshu",
    "age": 21,
    "skills": ["Python", "Editing", "Gaming"]
    }
}

print(profile["Himanshu"]["age"])

print("***************************")

for key, v in profile.items():
    print(f"{key} → {v}")
    
for key in profile:
    print(key, "→", profile[key])

