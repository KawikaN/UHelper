document.addEventListener("DOMContentLoaded", function () {
    const weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    const datesBox = document.querySelector(".dates-box");
    const bigBox = document.querySelector(".big-box");
    const DICTIONARY_KEY = "persistentDictionary";

    let userEvents = JSON.parse(localStorage.getItem(DICTIONARY_KEY)) || {};

    function saveDictionary() {
        console.log('Saving to localStorage:', JSON.stringify(userEvents));
        localStorage.setItem(DICTIONARY_KEY, JSON.stringify(userEvents)); // Save to localStorage
    }

    weekdays.forEach(day => {
        const dayDiv = document.createElement("div");
        dayDiv.className = "box";
        dayDiv.textContent = day;
        datesBox.appendChild(dayDiv);
    });

    const currentDate = new Date();
    let currentMonthIndex = currentDate.getMonth();
    const monthNames = months;
    const month = document.querySelector(".month");
    month.textContent = monthNames[currentMonthIndex];

    // Function to load events for a specific month
    function loadMonthEvents(monthIndex) {
        bigBox.innerHTML = '';  // Clear the current month content
        month.textContent = monthNames[monthIndex];

        const daysInMonth = new Date(currentDate.getFullYear(), monthIndex + 1, 0).getDate();

        for (let i = 1; i <= daysInMonth; i++) {
            const dateKey = `${currentDate.getFullYear()}-${monthIndex + 1}-${i}`;  // Use a date format like "YYYY-MM-DD"
            const dateDiv = document.createElement("div");
            dateDiv.className = "box";
            const dateContent = document.createElement("div");
            dateContent.className = "date";
            dateContent.textContent = i;

            const eventsContainer = document.createElement("div");
            eventsContainer.className = "events";
            dateDiv.appendChild(dateContent);
            dateDiv.appendChild(eventsContainer);
            bigBox.appendChild(dateDiv);

            const data = JSON.parse(document.getElementById('dueDates').value);

            for (let title in data) {
                const date = data[title];
                const shortMonth = monthNames[monthIndex].substring(0, 3);
                const sD = date.substring(0, 3);
                const eventDay = parseInt(date.substring(4, 6).trim(), 10);

                if (sD === shortMonth && eventDay === i) {
                    if (!userEvents[dateKey]?.event?.includes(title)) {
                        if (userEvents[dateKey]) {
                            userEvents[dateKey].event.push(title);
                        } else {
                            userEvents[dateKey] = { month: monthNames[monthIndex], event: [title] };
                        }
                    }
                }
            }

            if (userEvents[dateKey]) {
                const userEvent = userEvents[dateKey];
                const events = Array.isArray(userEvent.event) ? userEvent.event : [userEvent.event];

                events.forEach((event) => {
                    if (!Array.from(eventsContainer.children).some(e => e.textContent === `• ${event}`)) {
                        const eventItem = document.createElement("div");
                        eventItem.className = "event-item";
                        if(event.length > 12){
                            event = event.substring(0, 12);
                            eventItem.textContent = `• ${event}..`;
                        }
                        else{
                            eventItem.textContent = `• ${event}`;
                        }
                        eventsContainer.appendChild(eventItem);

                        eventItem.addEventListener("click", (e) => {
                            const existingTaskbar = document.querySelector('.taskbar');
                            if (existingTaskbar) existingTaskbar.remove();

                            const taskbar = document.createElement('div');
                            const rect = eventItem.getBoundingClientRect();
                            taskbar.style.left = `${rect.left}px`;
                            taskbar.style.top = `${rect.top - taskbar.offsetHeight - 10}px`;
                            taskbar.className = 'taskbar';
                            taskbar.innerHTML = `
                                <div class="taskbar-item">X</div>
                                <div class="taskbar-item">Option 2</div>
                            `;
                            eventItem.appendChild(taskbar);

                            const taskbarItems = taskbar.querySelectorAll('.taskbar-item');
                            taskbarItems.forEach((item, index) => {
                                item.addEventListener('click', () => {
                                    if (index == 0) {
                                        const eventIndex = userEvents[dateKey].event.indexOf(event);
                                        if (eventIndex !== -1) {
                                            userEvents[dateKey].event.splice(eventIndex, 1);
                                            if (userEvents[dateKey].event.length === 0) {
                                                delete userEvents[dateKey];
                                            }
                                            saveDictionary();
                                            eventItem.remove();
                                        }
                                    }
                                });
                            });

                            document.addEventListener('click', () => {
                                const taskbar = document.querySelector('.taskbar');
                                if (taskbar) taskbar.remove();
                            }, { once: true });

                            e.stopPropagation(); // Ensure clicks on taskbar don't trigger dateDiv click
                        });
                    }
                });
            }

            // Handle adding new events
            dateDiv.addEventListener("click", () => {
                const eventInput = document.createElement('input');
                eventInput.type = "text";
                eventInput.placeholder = "Type here and press Enter";
                dateDiv.appendChild(eventInput);

                const rect = eventInput.getBoundingClientRect();
                eventInput.style.left = `${rect.left}px`;
                eventInput.style.top = `${rect.top - eventInput.offsetHeight + 20}px`;
                eventInput.focus();

                eventInput.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter' && eventInput.value) {
                        const eventText = eventInput.value;
                        const eventItem = document.createElement("div");
                        eventItem.className = "event-item";
                        if(eventText.length > 12){
                            eventText = eventText.substring(0, 12);
                            eventItem.textContent = `• ${eventText}..`;
                        }
                        else{
                            eventItem.textContent = `• ${eventText}`;
                        }
                        eventsContainer.appendChild(eventItem);

                        if (userEvents[dateKey]) {
                            userEvents[dateKey].event.push(eventText);
                        } else {
                            userEvents[dateKey] = { month: monthNames[currentMonthIndex], event: [eventText] };
                        }

                        saveDictionary();

                        eventItem.addEventListener("click", (e) => {
                            const existingTaskbar = document.querySelector('.taskbar');
                            if (existingTaskbar) existingTaskbar.remove();

                            const taskbar = document.createElement('div');
                            const rect = eventItem.getBoundingClientRect();
                            taskbar.style.left = `${rect.left}px`;
                            taskbar.style.top = `${rect.top - taskbar.offsetHeight - 10}px`;
                            taskbar.className = 'taskbar';
                            taskbar.innerHTML = `
                                <div class="taskbar-item">X</div>
                                <div class="taskbar-item">Option 2</div>
                            `;
                            eventItem.appendChild(taskbar);

                            const taskbarItems = taskbar.querySelectorAll('.taskbar-item');
                            taskbarItems.forEach((item, index) => {
                                item.addEventListener('click', () => {
                                    if (index === 0) {
                                        const eventIndex = userEvents[dateKey].event.indexOf(eventText);
                                        if (eventIndex !== -1) {
                                            userEvents[dateKey].event.splice(eventIndex, 1);

                                            if (userEvents[dateKey].event.length === 0) {
                                                delete userEvents[dateKey];
                                            }

                                            saveDictionary();
                                            eventItem.remove();
                                        }
                                    }
                                });
                            });

                            document.addEventListener('click', () => {
                                const taskbar = document.querySelector('.taskbar');
                                if (taskbar) taskbar.remove();
                            }, { once: true });

                            e.stopPropagation();
                        });

                        eventInput.remove(); // Remove the input element after adding the event

                    }
                });
            });
        }
    }

    // Load events for the current month
    loadMonthEvents(currentMonthIndex);

    // Handle navigation between months
    document.querySelector(".r-arrow").addEventListener("click", () => {
        currentMonthIndex = (currentMonthIndex + 1) % 12;
        loadMonthEvents(currentMonthIndex);
    });

    document.querySelector(".l-arrow").addEventListener("click", () => {
        currentMonthIndex = (currentMonthIndex - 1 + 12) % 12;
        loadMonthEvents(currentMonthIndex);
    });

    document.querySelector(".clear").addEventListener("click", () => {
        Object.keys(userEvents).forEach(day => {
            if (userEvents[day].month === monthNames[currentMonthIndex]) {
                delete userEvents[day];
            }
        });
        saveDictionary();
        location.reload(true);
    });
});
