python -m pip install psutil

git clone https://github.com/Devarsh-leo/news-feed-extractor-worker.git
git clone https://github.com/parthshah7551/news-feed-extractor-backend.git
git clone https://github.com/parthshah7551/news-feed-extractor-frontend.git

cd news-feed-extractor-worker
call setup.bat

cd ..
call frontend-setup.bat

cd ../news-feed-extractor-backend
npm install
