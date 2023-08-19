export const GasPlanet = (props) => {
    
    return (
        <div>
            {props.planets.map(
                (planet, key) => {
                    return planet.isGasPlanet && <p key={key}>{planet.name}</p>
                }
            )}
        </div>
    );
}