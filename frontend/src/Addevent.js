import React, {useState, useEffect, useRef} from "react";
import {BASE_API_URL, PRIVATE_EVENTS, PRIVATE_PLACES, TAGS} from "./const";
import {getPrivateItems, getTagItems} from "./api";
import {useHistory} from "react-router-dom";


const Send = ({current}, callback) => {
// Функция send отправляет данные из формы в api

  const getValue = name => {
  //Функция для заполнения данными из формы объекта
    return current.elements.namedItem(name).value;
  };

  //Получение значений select multiple
  const selected = document.querySelectorAll('#FormControlSelect2 option:checked');
  const tags = Array.from(selected).map(el => el.value);
  console.log(tags);
  //
  let time = getValue("time");
  console.log(time);
  let date = getValue("date");
  console.log(date);
  let event_time = date + "T" + time + ":00Z";
  console.log(event_time);

  let event = {
    "title": getValue("title"),
    "body": getValue("body"),
    "place": getValue("place"),
    "tags": tags,
    "event_time": event_time
  };
  const token = window.localStorage.getItem('token');

  fetch(`${BASE_API_URL}${PRIVATE_EVENTS}`, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json; charset=utf-8',
      'Authorization': `Token ${token}`
    },
    body: JSON.stringify(event)
  })
    .then(response => response.json())
    .then(json => callback(json));

};


function PushPlaces({place_name}) {
  return (<option>{place_name}</option>)
}

function PushTags({title}) {
  return (<option>{title}</option>)
}


function EventForm() {
// Здесь я объявляю переменные для отправки
  const formRef = useRef(null);
  const history = useHistory();
//В этом блоке я подгружаю все известные места в форму
  const [places, setPlaces] = useState([]);
  const [tags, setTags] = useState([]);
  const [path, _] = useState(PRIVATE_PLACES);
  const [path_tags,] = useState(TAGS);
  const [url, setURL] = useState(null);
  const token = window.localStorage.getItem('token');

  useEffect(() => {
    getPrivateItems({ url, path, token }, (j) => setPlaces(j.results))
  }, [path]);


  useEffect(() => {
    getTagItems({path_tags}, (j) => setTags(j.results))
  }, [path_tags]);

//
  return (
    <form className="App" ref={formRef} id="eventForm">
      <div className="form-row">
        <div className="form-group col-md-6">
          <label htmlFor="input_event_name">Наименование события</label>
          <input
            className="form-control"
            name="title"
            type="text"
          />
        </div>
        <div className="form-group col-md-3">
          <p>
            <label htmlFor="input_date">Дата проведения</label>
            <input
              className="form-control"
              name="date"
              type="date"
            />
          </p>
        </div>
        <div className="form-group col-md-3">
          <p>
            <label htmlFor="input_time">Время начала</label>
            <input
              className="form-control"
              name="time"
              type="time"
            />
          </p>
        </div>
      </div>

      <div className="form-group">
        <div className="input-group">
          <div className="input-group-prepend">
            <span className="input-group-text">Описание события</span>
          </div>
          <textarea
            className="form-control"
            aria-label="input-group-text"
            name="body"
          />
        </div>
      </div>
      <div className="form-row">
        <div className="form-group col-md-6">
          <label htmlFor="FormControlSelect1">Выберите место проведения:</label>
          <select className="form-control" id="FormControlSelect1" name="place">
            <option>Выбрать</option>
            {places.map((e, i) => <PushPlaces {...e}/>)}
          </select>
        </div>
          <div className="form-group col-md-6">
          <label htmlFor="FormControlSelect2">Выберите подходящие тэги:</label>
          <select className="form-control" id="FormControlSelect2" name="tags" multiple="multiple" >
            {tags.map((e, i) => <PushTags {...e}/>)}
          </select>
        </div>
      </div>
      <button type="submit" className="btn btn-primary" onClick={
        () => Send(formRef, () => history.push('/events'))
      }>Send</button>
    </form>
  );
}

function AddEvent() {
  return (
  <>
    <div className="container">
      <div className="my-h1">
        <h3 style={{textAlign: "center", marginBottom: 30, marginTop: 20}}>
          Форма для добавления Событий
        </h3>
      </div>
      <EventForm />
    </div>
  </>
  )
}

export default AddEvent
