#!/usr/bin/bash -x
echo wrapper3000 > s3_wordlist
bucket_finder/bucket_finder.rb s3_wordlist
bucket_finder/bucket_finder.rb --download s3_wordlist
