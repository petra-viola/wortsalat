def count_affiliative_humor(text: str) -> int:
    affiliative_humor_count = sum(1 for word in text.split() if word == "lustig")
    return affiliative_humor_count

text = "Das hier ist witzig."
affiliative_humor_count = count_affiliative_humor(text)
print(f"Affiliativer Humor: {affiliative_humor_count}")
