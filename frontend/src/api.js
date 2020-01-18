const BASE_API_URL = 'http://127.0.0.1:8000/api/v1';

export const getItems = ({ url, path }, callback) => {
  const fullUrl = url || `${BASE_API_URL}${path}`;
  fetch(fullUrl)
    .then(result => result.json())
    .then(json => {
      callback(json);
    })
    .catch(e => console.log(e));
};
