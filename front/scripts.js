/*
  --------------------------------------------------------------------------------------
  Global Variables
  --------------------------------------------------------------------------------------
*/
const attributes = Object.freeze({
  Id: 1, 
  Surface: 2,
  TourneyYear: 3,
  TourneyLevel: 4,
  BestOfXSets: 5,
  TourneyRound: 6,
  FirstName: 7,
  FisrtId: 8,
  FirstRank: 9,
  FirstRankPoints: 10,
  FirstHand: 11,
  FirstHeight: 12,
  FirstAge: 13,
  SecondId: 14,
  SecondRank: 15,
  SecondRankPoints: 16,
  SecondHand: 17,
  SecondHeight: 18,
  SecondAge: 19,
  Winner: 20
});


/*
  --------------------------------------------------------------------------------------
  Function to get a match from the server database, via GET request
  --------------------------------------------------------------------------------------
*/
const getItem = async function (item_id) {
  console.log(item_id);
  let item = {};
  let url = 'http://127.0.0.1:5000/match?id=' + item_id;
  await fetch(url, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      item.id = data.id;
      item.surface = data.surface;
      item.year = data.year;
      item.tourney_level = data.tourney_level;
      item.best_of_x_sets = data.best_of_x_sets;
      item.tourney_round = data.tourney_round;
      item.first_name = data.first_name;
      item.first_id = data.first_id;
      item.first_rank = data.first_rank;
      item.first_rank_points = data.first_rank_points;
      item.first_hand = data.first_hand;
      item.first_height = data.first_height;
      item.first_age = data.first_age;
      item.second_name = data.second_name;
      item.second_id = data.second_id;
      item.second_rank = data.second_rank;
      item.second_rank_points = data.second_rank_points;
      item.second_hand = data.second_hand;
      item.second_height = data.second_height;
      item.second_age = data.second_age;
      item.winner = data.winner;
    })

  return item;
}


/*
  --------------------------------------------------------------------------------------
  Function to obtain the list of existing matches from the server database, via GET request
  --------------------------------------------------------------------------------------
*/
const getList = async () => {

  let url = 'http://127.0.0.1:5000/matches';
  await fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.matches.forEach(item => insertItemInterface(item.id, item.surface, item.year,
                                                        item.tourney_level, item.best_of_x_sets, item.tourney_round,
                                                        item.first_name, item.first_id, item.first_rank, item.first_rank_points,
                                                        item.first_hand, item.first_height, item.first_age,
                                                        item.second_name, item.second_id, item.second_rank, item.second_rank_points,
                                                        item.second_hand, item.second_height, item.second_age,
                                                        item.winner));
      connectDeleteFunctionsToButtons();
      connectEditFunctionsToButtons();
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Function to clear the "new match" insertion form
  --------------------------------------------------------------------------------------
*/
const clearForm = () => {
  document.getElementById("newSurface").value = "";
  document.getElementById("newTourneyYear").value = "";
  document.getElementById("newTourneyLevel").value = "";
  document.getElementById("newBestOfXSets").value = "";
  document.getElementById("newTourneyRound").value = "";
  document.getElementById("newFirstName").value = "";
  document.getElementById("newFirstId").value = "";
  document.getElementById("newFirstRank").value = "";
  document.getElementById("newFirstRankPoints").value = "";
  document.getElementById("newFirstHand").value = "";
  document.getElementById("newFirstHeight").value = "";
  document.getElementById("newFirstAge").value = "";
  document.getElementById("newSecondName").value = "";
  document.getElementById("newSecondId").value = "";
  document.getElementById("newSecondRank").value = "";
  document.getElementById("newSecondRankPoints").value = "";
  document.getElementById("newSecondHand").value = "";
  document.getElementById("newSecondHeight").value = "";
  document.getElementById("newSecondAge").value = "";
}


/*
  --------------------------------------------------------------------------------------
  Function to insert new match, first in the interface
  (with insertItemInterface()), and then on the server bank (with postItem())
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let input_surface = document.getElementById("newSurface").value;
  let input_year = document.getElementById("newTourneyYear").value;
  let input_tourney_level = document.getElementById("newTourneyLevel").value;
  let input_best_of_x_sets = document.getElementById("newBestOfXSets").value;
  let input_tourney_round = document.getElementById("newTourneyRound").value;
  let input_first_name = document.getElementById("newFirstName").value;
  let input_first_id = document.getElementById("newFirstId").value;
  let input_first_rank = document.getElementById("newFirstRank").value;
  let input_first_rank_points = document.getElementById("newFirstRankPoints").value;
  let input_first_hand = document.getElementById("newFirstHand").value;
  let input_first_height = document.getElementById("newFirstHeight").value;
  let input_first_age = document.getElementById("newFirstAge").value;
  let input_second_name = document.getElementById("newSecondName").value;
  let input_second_id = document.getElementById("newSecondId").value;
  let input_second_rank = document.getElementById("newSecondRank").value;
  let input_second_rank_points = document.getElementById("newSecondRankPoints").value;
  let input_second_hand = document.getElementById("newSecondHand").value;
  let input_second_height = document.getElementById("newSecondHeight").value;
  let input_second_age = document.getElementById("newSecondAge").value;

  const input_list = [
    input_surface,
    input_year,
    input_tourney_level,
    input_best_of_x_sets,
    input_tourney_round,
    input_first_name,
    input_first_id,
    input_first_rank,
    input_first_rank_points,
    input_first_hand,
    input_first_height,
    input_first_age,
    input_second_name,
    input_second_id,
    input_second_rank,
    input_second_rank_points,
    input_second_hand,
    input_second_height,
    input_second_age
  ]

  let is_input_valid = true;
  for (let idx = 0; idx < input_list.length; idx++) {
    if (input_list[idx] === '') {
      is_input_valid = false;
    }
  }

  if (!is_input_valid) {
    alert("All fields are mandatory! Please check your form!");
  } else {
    let new_item = await postItem(
      input_surface,
      input_year,
      input_tourney_level,
      input_best_of_x_sets,
      input_tourney_round,
      input_first_name,
      input_first_id,
      input_first_rank,
      input_first_rank_points,
      input_first_hand,
      input_first_height,
      input_first_age,
      input_second_name,
      input_second_id,
      input_second_rank,
      input_second_rank_points,
      input_second_hand,
      input_second_height,
      input_second_age);

    insertItemInterface(
      new_item.id,
      new_item.surface,
      new_item.year,
      new_item.tourney_level,
      new_item.best_of_x_sets,
      new_item.tourney_round,
      new_item.first_name,
      new_item.first_id,
      new_item.first_rank,
      new_item.first_rank_points,
      new_item.first_hand,
      new_item.first_height,
      new_item.first_age,
      new_item.second_name,
      new_item.second_id,
      new_item.second_rank,
      new_item.second_rank_points,
      new_item.second_hand,
      new_item.second_height,
      new_item.second_age,
      new_item.winner);

    connectDeleteFunctionsToButtons();
    connectEditFunctionsToButtons();
    alert("New match added!");
  }
}


/*
  --------------------------------------------------------------------------------------
  Function to edit match, first in the interface
  (with insertItemInterface()), and then on the server bank (with postItem())
  --------------------------------------------------------------------------------------
*/
const editItem = async () => {
  let input_surface = document.getElementById("newSurface").value;
  let input_year = document.getElementById("newTourneyYear").value;
  let input_tourney_level = document.getElementById("newTourneyLevel").value;
  let input_best_of_x_sets = document.getElementById("newBestOfXSets").value;
  let input_tourney_round = document.getElementById("newTourneyRound").value;
  let input_first_name = document.getElementById("newFirstName").value;
  let input_first_id = document.getElementById("newFirstId").value;
  let input_first_rank = document.getElementById("newFirstRank").value;
  let input_first_rank_points = document.getElementById("newFirstRankPoints").value;
  let input_first_hand = document.getElementById("newFirstHand").value;
  let input_first_height = document.getElementById("newFirstHeight").value;
  let input_first_age = document.getElementById("newFirstAge").value;
  let input_second_name = document.getElementById("newSecondName").value;
  let input_second_id = document.getElementById("newSecondId").value;
  let input_second_rank = document.getElementById("newSecondRank").value;
  let input_second_rank_points = document.getElementById("newSecondRankPoints").value;
  let input_second_hand = document.getElementById("newSecondHand").value;
  let input_second_height = document.getElementById("newSecondHeight").value;
  let input_second_age = document.getElementById("newSecondAge").value;
  let item_id = document.getElementById("editedItemId").value;

  if (!confirm("Confirm the changes to match #" + item_id + " (" + input_first_name + " vs " + input_second_name +")?")) {
    return;
  }

  const input_list = [
    input_surface,
    input_year,
    input_tourney_level,
    input_best_of_x_sets,
    input_tourney_round,
    input_first_name,
    input_first_id,
    input_first_rank,
    input_first_rank_points,
    input_first_hand,
    input_first_height,
    input_first_age,
    input_second_name,
    input_second_id,
    input_second_rank,
    input_second_rank_points,
    input_second_hand,
    input_second_height,
    input_second_age
  ]

  let is_input_valid = true;
  for (let idx = 0; idx < input_list.length; idx++) {
    if (input_list[idx] === '') {
      is_input_valid = false;
    }
  }

  if (!is_input_valid) {
    alert("All fields are mandatory! Please check your form!");
  } else {
    let new_item = await putItem(
      input_surface,
      input_year,
      input_tourney_level,
      input_best_of_x_sets,
      input_tourney_round,
      input_first_name,
      input_first_id,
      input_first_rank,
      input_first_rank_points,
      input_first_hand,
      input_first_height,
      input_first_age,
      input_second_name,
      input_second_id,
      input_second_rank,
      input_second_rank_points,
      input_second_hand,
      input_second_height,
      input_second_age,
      item_id);
    
    // TODO [MVP3-20]: improve code by updating only the edited match in the interface
    let table = document.getElementById('table-matches');
    for (let i = table.rows.length - 1; i > 0; i--) {
      table.deleteRow(i);
    }

    getList();

    // Controls displayed interface/buttons in edition mode
    let add_button = document.getElementById("addBtn");
    let finish_edition_button = document.getElementById("editBtn");
    let cancel_edition_button = document.getElementById("cancelEditBtn");
    let id_form = document.getElementById("editedItemId");
    let id_form_label = document.getElementById("editedItemIdLabel");
    add_button.style.display = "inline";
    finish_edition_button.style.display = "none";
    cancel_edition_button.style.display = "none";
    id_form.style.display = "none";
    id_form_label.style.display = "none";
    clearForm();

    alert("Match edited!");
  }
}


/*
  --------------------------------------------------------------------------------------
  Function to insert new match, first in the interface
  (with insertItemInterface()), and then on the server bank (with postItem())
  --------------------------------------------------------------------------------------
*/
const cancelEdition = async () => {
  // Controls displayed interface/buttons in edition mode
  let add_button = document.getElementById("addBtn");
  let finish_edition_button = document.getElementById("editBtn");
  let cancel_edition_button = document.getElementById("cancelEditBtn");
  let id_form = document.getElementById("editedItemId");
  let id_form_label = document.getElementById("editedItemIdLabel");
  add_button.style.display = "inline";
  finish_edition_button.style.display = "none";
  cancel_edition_button.style.display = "none";
  id_form.style.display = "none";
  id_form_label.style.display = "none";
  clearForm();
  alert("Edition canceled!");
}


/*
  --------------------------------------------------------------------------------------
  Function to add new match in the server database, via POST request
  --------------------------------------------------------------------------------------
*/
const postItem = async (surface, year, tourney_level, best_of_x_sets, tourney_round,
                        first_name, first_id, first_rank, first_rank_points, first_hand, first_height, first_age,
                        second_name, second_id, second_rank, second_rank_points, second_hand, second_height, second_age) => {
  const formData = new FormData();
  formData.append('surface', surface);
  formData.append('year', year);
  formData.append('tourney_level', tourney_level);
  formData.append('best_of_x_sets', best_of_x_sets);
  formData.append('tourney_round', tourney_round);
  formData.append('first_name', first_name);
  formData.append('first_id', first_id);
  formData.append('first_rank', first_rank);
  formData.append('first_rank_points', first_rank_points);
  formData.append('first_hand', first_hand);
  formData.append('first_height', first_height);
  formData.append('first_age', first_age);
  formData.append('second_name', second_name);
  formData.append('second_id', second_id);
  formData.append('second_rank', second_rank);
  formData.append('second_rank_points', second_rank_points);
  formData.append('second_hand', second_hand);
  formData.append('second_height', second_height);
  formData.append('second_age', second_age);
  let new_match = {};

  let url = 'http://127.0.0.1:5000/match';
  await fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .then((data) => {
      new_match = data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });

  return new_match;
}


/*
  --------------------------------------------------------------------------------------
  Function to edit match in the server database, via PUT request
  --------------------------------------------------------------------------------------
*/
const putItem = async (surface, year, tourney_level, best_of_x_sets, tourney_round,
                       first_name, first_id, first_rank, first_rank_points, first_hand, first_height, first_age,
                       second_name, second_id, second_rank, second_rank_points, second_hand, second_height, second_age,
                       item_id) => {
  const formData = new FormData();
  formData.append('surface', surface);
  formData.append('year', year);
  formData.append('tourney_level', tourney_level);
  formData.append('best_of_x_sets', best_of_x_sets);
  formData.append('tourney_round', tourney_round);
  formData.append('first_name', first_name);
  formData.append('first_id', first_id);
  formData.append('first_rank', first_rank);
  formData.append('first_rank_points', first_rank_points);
  formData.append('first_hand', first_hand);
  formData.append('first_height', first_height);
  formData.append('first_age', first_age);
  formData.append('second_name', second_name);
  formData.append('second_id', second_id);
  formData.append('second_rank', second_rank);
  formData.append('second_rank_points', second_rank_points);
  formData.append('second_hand', second_hand);
  formData.append('second_height', second_height);
  formData.append('second_age', second_age);
  let edited_match = {};

  let url = 'http://127.0.0.1:5000/matchedition?id=' + item_id;
  await fetch(url, {
    method: 'put',
    body: formData
  })
    .then((response) => response.json())
    .then((data) => {
      edited_match = data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });

  return edited_match;
}


/*
  --------------------------------------------------------------------------------------
  Function to insert new match in the interface
  --------------------------------------------------------------------------------------
*/
const insertItemInterface = (id, surface, year, tourney_level, best_of_x_sets, tourney_round,
                             first_name, first_id, first_rank, first_rank_points, first_hand, first_height, first_age,
                             second_name, second_id, second_rank, second_rank_points, second_hand, second_height, second_age,
                             winner) => {
  let table = document.getElementById('table-matches');
  let row = table.insertRow();
  const item = [id, surface, year, tourney_level, best_of_x_sets, tourney_round,
                first_name, first_id, first_rank, first_rank_points, first_hand, first_height, first_age,
                second_name, second_id, second_rank, second_rank_points, second_hand, second_height, second_age,
                winner];
  const row_data_length = item.length;

  // Inserts 'edition' button at the beginning of each line of the UI matches table
  insertEditionItemButton(row.insertCell(0));
  
  // Inserts cells corresponding to each attribute in a row of the UI matches table
  for (var cell_idx = 1; cell_idx <= row_data_length; cell_idx++) {
    var cel = row.insertCell(cell_idx);

    // There are 10 cells/columns per row, but only 8 data values from the itens (1st cell is edition button and last cell is delete button)
    const item_idx = cell_idx - 1;
    const attribute_value = item[item_idx];
    cel.textContent = attribute_value;
  }

  // Inserts 'delete' button at the end of each line of the UI matches table
  insertDeleteItemButton(row.insertCell(-1));

  clearForm();
}


/*
  --------------------------------------------------------------------------------------
  Function to create a 'delete' button on each line of the UI matches table
  --------------------------------------------------------------------------------------
*/
const insertDeleteItemButton = (parent) => {
  let img = document.createElement("img");
  img.className = "bt-delete";
  img.src = "./img/delete.png";
  parent.appendChild(img);
}


/*
  --------------------------------------------------------------------------------------
  Function to create a 'edition' button on each line of the UI matches table
  --------------------------------------------------------------------------------------
*/
const insertEditionItemButton = (parent) => {
  let img = document.createElement("img");
  img.className = "bt-edit";
  img.src = "./img/edition.png";
  parent.appendChild(img);
}


/*
  --------------------------------------------------------------------------------------
  Create function to delete match and connect it to each 'delete' button in the interface
  --------------------------------------------------------------------------------------
*/
const connectDeleteFunctionsToButtons = () => {
  let delete_button = document.getElementsByClassName("bt-delete");
  let i;
  for (i = 0; i < delete_button.length; i++) {
    delete_button[i].onclick = function () {
      let current_row = this.parentElement.parentElement;
      const item_id_idx = 1;
      const item_id = current_row.getElementsByTagName('td')[item_id_idx].innerHTML;
      if (confirm("Are you sure? Confirm deletion?")) {
        current_row.remove();
        deleteItem(item_id);

        // Verifies if deleted item was being edited in edition mode
        const edited_item_id = document.getElementById("editedItemId").value;
        const is_edited_item_deleted = (edited_item_id === item_id);
        if (is_edited_item_deleted) {
          // Controls displayed interface/buttonsbutton in edition mode // FIXME: transform this into a function
          let add_button = document.getElementById("addBtn");
          let finish_edition_button = document.getElementById("editBtn");
          let cancel_edition_button = document.getElementById("cancelEditBtn");
          let id_form = document.getElementById("editedItemId");
          let id_form_label = document.getElementById("editedItemIdLabel");
          add_button.style.display = "inline";
          finish_edition_button.style.display = "none";
          cancel_edition_button.style.display = "none";
          id_form.style.display = "none";
          id_form_label.style.display = "none";
          clearForm();
        }

        alert("Match deleted!");
      }
    }
  }
}


/*
  --------------------------------------------------------------------------------------
  Create function to edit match and connect it to each 'edition' button in the interface
  --------------------------------------------------------------------------------------
*/
const connectEditFunctionsToButtons = () => {
  let item_edit_buttons = document.getElementsByClassName("bt-edit");
  let add_button = document.getElementById("addBtn");
  let finish_edition_button = document.getElementById("editBtn");
  let cancel_edition_button = document.getElementById("cancelEditBtn");
  let id_form = document.getElementById("editedItemId");
  let id_form_label = document.getElementById("editedItemIdLabel");

  for (let i = 0; i < item_edit_buttons.length; i++) {
    item_edit_buttons[i].onclick = async function () {

      // Controls displayed interface/buttonsbutton in edition mode
      add_button.style.display = "none";
      finish_edition_button.style.display = "inline";
      cancel_edition_button.style.display = "inline";
      id_form.style.display = "inline";
      id_form_label.style.display = "inline";
      
      // Get selected item data from table - better to do it from database
      // FIXME: Somehow get the ID into the "Finish Edition" function, it's necessary for the PUT request call
      let current_row = this.parentElement.parentElement;
      const row_attributes = current_row.getElementsByTagName('td')
      const item_id = row_attributes[attributes.Id].innerHTML;
      let item = await getItem(item_id);
      
      // Fill up edition form with selected item data
      document.getElementById("editedItemId").value = item.id;
      document.getElementById("newSurface").value = item.surface;
      document.getElementById("newTourneyYear").value = item.year;
      document.getElementById("newTourneyLevel").value = item.tourney_level;
      document.getElementById("newBestOfXSets").value = item.best_of_x_sets;
      document.getElementById("newTourneyRound").value = item.tourney_round;
      document.getElementById("newFirstName").value = item.first_name;
      document.getElementById("newFirstId").value = item.first_id;
      document.getElementById("newFirstRank").value = item.first_rank;
      document.getElementById("newFirstRankPoints").value = item.first_rank_points;
      document.getElementById("newFirstHand").value = item.first_hand;
      document.getElementById("newFirstHeight").value = item.first_height;
      document.getElementById("newFirstAge").value = item.first_age;
      document.getElementById("newSecondName").value = item.second_name;
      document.getElementById("newSecondId").value = item.second_id;
      document.getElementById("newSecondRank").value = item.second_rank;
      document.getElementById("newSecondRankPoints").value = item.second_rank_points;
      document.getElementById("newSecondHand").value = item.second_hand;
      document.getElementById("newSecondHeight").value = item.second_height;
      document.getElementById("newSecondAge").value = item.second_age;
    }
  }
}


/*
  --------------------------------------------------------------------------------------
  Function to delete a match from the server database, via DELETE request
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item_id) => {
  console.log(item_id);
  let url = 'http://127.0.0.1:5000/match?id=' + item_id;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Function to download/open csv file with player ID data
  --------------------------------------------------------------------------------------
*/
const openCSVFile = () => {
  let csvFilePath = 'resources/atp_players_till_2022.csv';
  window.open(csvFilePath, '_blank');
}


/*
  --------------------------------------------------------------------------------------
  Function call for initial loading of the UI matches table
  --------------------------------------------------------------------------------------
*/
getList();
