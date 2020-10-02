curl --request POST \
  --url https://www.virustotal.com/api/v3/urls \
  --header 'x-apikey: 4aa0e939e7ca150317b69c354d5d13c02f209008b660bc8ea16918da828b1336' \
  --form url='https://www.youtube.com/watch?v=076Y3aaDNCw'



curl --request GET \
  --url https://www.virustotal.com/api/v3/ip_addresses/{192.168.72.1} \
  --header 'x-apikey: 4aa0e939e7ca150317b69c354d5d13c02f209008b660bc8ea16918da828b1336'

curl --request POST \
  --url https://www.virustotal.com/api/v3/urls \
  --header 'x-apikey: 4aa0e939e7ca150317b69c354d5d13c02f209008b660bc8ea16918da828b1336' \
  --form url='https://www.google.com/'

