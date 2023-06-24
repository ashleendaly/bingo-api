interface Incident {
  id: string;
  label: string;
  count: number;
}

interface Player {
  id: string;
  name: string;
}

interface addIncident {
  type: "addIncident";
  incident: Incident;
}

interface removeIncident {
  type: "removeIncident";
  incident: Incident;
}

interface incidentOccurrence {
  type: "incidentOccurrence";
  incident: Incident;
}

interface playerJoin {
  type: "playerJoin";
  player: Player;
}

interface playerLeave {
  type: "playerLeave";
  player: Player;
}

interface gameStart {
  type: "gameStart";
}

interface gameEnd {
  type: "gameEnd";
}

interface gameWon {
  type: "gameWon";
  player: Player;
}

interface handshake {
  type: "handshake";
  players: Player[];
  incidents: Incident[];
  code: string;
}

type event =
  | addIncident
  | removeIncident
  | incidentOccurrence
  | playerJoin
  | playerLeave
  | gameStart
  | gameEnd
  | gameWon
  | handshake;
