def unique_email_addresses(emails):
    """
    https://leetcode.com/problems/unique-email-addresses/
    """
    num_sent = 0
    sent = set()
    for email in emails:
        local_name, domain_name = email.split("@")
        treated_local_name = _treat_local_name(local_name)
        collated_email = treated_local_name + domain_name
        if collated_email not in sent:
            sent.add(collated_email)
            num_sent += 1

    return num_sent


def _treat_local_name(local_name):
    return _remove_all_dots(_prune_plus_tails(local_name))


def _prune_plus_tails(local_name):
    for i, char in enumerate(local_name):
        if char == "+":
            return local_name[:i]

    return local_name


def _remove_all_dots(local_name):
    dotless_local_name = ""
    for char in local_name:
        if char == ".":
            continue

        dotless_local_name += char

    return dotless_local_name
