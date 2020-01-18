import React, {useState, useEffect} from "react";
import {BASE_API_URL} from "./const";
import SendForm from "./somesend";


const ADD_EVENT_ROUTE = 'add_event';

function SendPost(obj, url) {
  let xhr = new XMLHttpRequest();
  let json = JSON.stringify(obj);
  xhr.open("POST", url);
  xhr.setRequestHeader('Content-type', 'application/json');
  xhr.send(json);
  xhr.onreadystatechange = function()
  {
    if (xhr.readyState === 4) {
      if (xhr.status === 201) {
        alert('Отправлено:');
      }
    }
  }
}

class AddEvent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isEventName: '',
      isEventDate: '',
      isEventTime: '',
      isEventBody: '',
      isPlaceName: '',
      isPlaceCity: '',
      isPlaceStreet: '',
      isPlaceHouse: '',
      isPlaceOffice: '',
      isTag: ''
    };

    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleChanged() {
    let place = {
      "place_name": this.state.isPlaceName,
      "city": this.state.isPlaceCity,
      "street": this.state.isPlaceStreet,
      "house_number": this.state.isPlaceHouse,
      "office_number": this.state.isPlaceOffice
    };
    let url = "http://127.0.0.1:8000/api/v1/places/";
    SendPost(place, url);

    // alert('Event отправлено:'
    //   + this.state.isEventName + ';'
    //   + this.state.isEventDate + ';'
    //   + this.state.isEventTime + ';'
    //   + this.state.isEventBody + ';'
    //   + this.state.isTag + ';'
    // );
    // event.preventDefault();
  }

  render() {
    return (
      <form>
        <div className="form-row">
          <div className="form-group col-md-6">
            <label htmlFor="input_event_name">Наименование события</label>
            <input
              className="form-control"
              name="isEventName"
              type="text"
              checked={this.state.isEventName}
              onChange={this.handleInputChange}
            />
          </div>
          <div className="form-group col-md-3">
            <p>
              <label htmlFor="input_date">Дата проведения</label>
              <input
                className="form-control"
                name="isEventDate"
                type="date"
                checked={this.state.isEventDate}
                onChange={this.handleInputChange}
              />
            </p>
          </div>
          <div className="form-group col-md-3">
            <p>
              <label htmlFor="input_time">Время начала</label>
              <input
                className="form-control"
                name="isEventTime"
                type="time"
                checked={this.state.isEventTime}
                onChange={this.handleInputChange}
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
              name="isEventBody"
              checked={this.state.isEventBody}
              onChange={this.handleInputChange}
            />
          </div>
        </div>
        <div className="form-group">
          <label htmlFor="inputAddress">Место проведения</label>
          <input
            type="text"
            className="form-control"
            placeholder="Название"
            name="isPlaceName"
            checked={this.state.isPlaceName}
            onChange={this.handleInputChange}
          />
        </div>
        <div className="form-row">
          <div className="form-group col-md-4">
            <label htmlFor="inputCity">Город</label>
            <input
              type="text"
              className="form-control"
              name="isPlaceCity"
              checked={this.state.isPlaceCity}
              onChange={this.handleInputChange}
            />
          </div>
          <div className="form-group col-md-4">
            <label htmlFor="inputStreet">Улица</label>
            <input
              type="text"
              className="form-control"
              name="isPlaceStreet"
              checked={this.state.isPlaceStreet}
              onChange={this.handleInputChange}
            />
          </div>
          <div className="form-group col-md-2">
            <label htmlFor="inputStreet">Дом</label>
            <input
              type="text"
              className="form-control"
              name="isPlaceHouse"
              checked={this.state.isPlaceHouse}
              onChange={this.handleInputChange}
            />
          </div>
          <div className="form-group col-md-2">
            <label htmlFor="inputStreet">Офис</label>
            <input
              type="text"
              className="form-control"
              name="isPlaceOffice"
              checked={this.state.isPlaceOffice}
              onChange={this.handleInputChange}
            />
          </div>
          <div className="form-group col-md-4">
            <label htmlFor="inputState">Тэги</label>
            <input
              type="text"
              className="form-control"
              name="isTag"
              checked={this.state.isTag}
              onChange={this.handleInputChange}
            />
          </div>
        </div>
        <button type="submit" className="btn btn-primary" onClick={() => this.handleChanged()}>Send</button>
      </form>
    );
  }
  }

  function Add_event() {

    return (
    <>
      <div className="container">
        <div className="my-h1"><h3 style={{textAlign: "center"}}>Форма для добавления Событий</h3></div>
        < SendForm/>
        {/*< AddEvent />*/}
      </div>
    </>
    )
  }

  export default Add_event
  export {
    ADD_EVENT_ROUTE
  }