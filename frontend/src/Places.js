import React, {useEffect, useState} from 'react';
import {getItems} from "./api";
import Pagination from "./Pagination";
import {PLACES} from "./const";


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
  const path= PLACES;
  const [url, setURL] = useState(null);
  const [pagination, setPagination] = useState([null, null]);

  const fetchCallback = (j) => {
      setPlaces(j.results);
      setPagination([j.next, j.previous])
  };

  useEffect(() => {
    getItems({url, path}, fetchCallback)
  }, [url, path]);

  const [next, previous] = pagination;

  return (
    <>
      <div>
        <div className="my-h1">
          <h2 style={{textAlign: "center", marginBottom: 30, marginTop: 20}}>
            Список заведений
          </h2>
          <div className="row">
            {places.map((e, i) => <Place {...e}/>)}
          </div>
        </div>
        <Pagination
          next={next}
          previous={previous}
          setURL={setURL}
          />
      </div>
    </>
  )
}

export default Places

