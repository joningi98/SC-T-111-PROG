class FileOwners:

    @staticmethod
    def group_by_owners(files):
        new_dict = {}
        for file, name in files.items():
            if name in new_dict.keys():
                new_dict[name].append(file)
            else:
                new_dict[name] = [file]
        return new_dict


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
