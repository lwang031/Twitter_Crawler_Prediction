#$1 - chunk size
#$2 - chunk count

if (( $1 <= 0 )); then
	echo "Invalid chunk size. Must be positive integer";
	exit 1
fi

if (( $2 <= 0 )); then
	echo "Invalid chunk count. Must be positive integer";
	exit 1
fi

python twitterStream.py $1 $2