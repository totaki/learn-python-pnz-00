import React, {useEffect, useState} from 'react';
import {BASE_API_URL} from "./const";

const PLACES_ROUTE = 'places';

function Place({ place_name, city, street, house_number }) {
  return (
    <div className="col-md-4">
          <div className="card mb-4 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">{place_name}</h5>
              <p className="card-text">{city}, {street}, {house_number}</p>
            </div>
          </div>
        </div>

  )
}

function Places() {
   const [places, setPlaces] = useState([]);
   const [url, setURL] = useState(`${BASE_API_URL}/places/`);

   useEffect(() => {
    fetch(url)
      .then(result => result.json())
      .then(json => {
        setPlaces(json.results);
      })
      .catch(e => console.log(e));
  }, [url]);

   return (
    <>
      <div className="container">
        <div className="my-h1"><h1 style={{textAlign: "center"}}>Список заведений</h1></div>
          <div className="container">
            <div className="row">
              {places.map((e, i) => <Place {...e}/>)}
            </div>
          </div>
      </div>
    </>
  )
}

export default Places
export {
  PLACES_ROUTE
}
