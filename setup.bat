python -m pip install psutil

git clone https://github.com/Devarsh-leo/news-feed-extractor-worker.git
git clone https://github.com/parthshah7551/news-feed-extractor-backend.git
git clone https://github.com/parthshah7551/news-feed-extractor-frontend.git

cd news-feed-extractor-worker
call setup.bat
deactivate

cd ../news-feed-extractor-backend
npm i

cd ../news-feed-extractor-frontend
npm cache clean --force
npm i 
PAUSE