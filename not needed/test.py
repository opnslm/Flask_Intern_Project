from passlib.hash import pbkdf2_sha256

password = "1234"

hashedPass = pbkdf2_sha256.using(salt_size=16).hash(password)



print(pbkdf2_sha256.verify("123", hashedPass))