import { browser } from '@wdio/globals';
import { Given, Then, When } from '@wdio/cucumber-framework';
import fs from 'fs';

Given(/^DuckDuckGo page is opened$/, async () => {
    await browser.url('https://duckduckgo.com/');
    await browser.pause(1000);
});

When(/^I search with (.*)$/, async (searchItem: string) => {
    const searchInput = await browser.$(`[name=q]`);
    await searchInput.setValue(searchItem);
    await browser.keys('Enter');
    await browser.pause(1000);
});

When(/^I click on the first search result$/, async () => {
    const firstLink = await browser.$(`<h2>`);
    await firstLink.click();
    await browser.pause(10000);
});

Then(/^The URL should match (.*)$/, async (expectedURL: string) => {
    expect(await browser.getUrl()).toMatch(expectedURL); // old chai API method
    expect(browser).toHaveUrl(expectedURL); // expect-webdriverio API method
});

// text input interactions
Given(/^Text inputs page is open$/, async () => {
    await browser.url('https://the-internet.herokuapp.com/inputs');
    await browser.setTimeout({ implicit: 15000, pageLoad: 10000 });
    await browser.maximizeWindow();
});

When(/^Perform text input interactions$/, async () => {
    let el = await browser.$('[type=number]');
    // type into the input box
    await el.setValue('12345');
    await browser.pause(1000);

    // clear the field and type or just add value
    await el.clearValue();
    await browser.pause(1000);

    // add value
    await el.addValue('12345');
    await browser.pause(1000);

    // click
    await el.click();
    await browser.pause(1000);

    // delete one of the characters
    await browser.keys('Backspace');

    // slow typing
    for (let char of '123456') {
        await browser.pause(100);
        await browser.keys(char);
    }
});

Then(/^The text inputs should be filled$/, async () => {
    let el = await browser.$('[type=number]');
    expect(await el.getValue()).toBe('1234123456');
});

// dropdown interactions
Given(/^Dropdown page is open$/, async () => {
    await browser.url('https://the-internet.herokuapp.com/dropdown');
    await browser.setTimeout({ implicit: 15000, pageLoad: 10000 });
    await browser.maximizeWindow();
});

When(/^Check the default dropdown value$/, async () => {
    let dropdown = await browser.$('//select/option[@selected="selected"]');
    let value = await dropdown.getText();
    expect(value).toBe('Please select an option');
});

When(/^Perform dropdown interaction - select option 1$/, async () => {
    let dropdown = await browser.$('#dropdown');
    await dropdown.selectByVisibleText('Option 1');
});

Then(/^The new dropdown value should be 1$/, async () => {
    let dropdown = await browser.$('#dropdown');
    expect(await dropdown.getValue()).toBe('1');
});

When(/^Perform dropdown interaction - select option 2$/, async () => {
    let dropdown = await browser.$('#dropdown');
    await dropdown.selectByIndex(2);
});

Then(/^The new dropdown value should be 2$/, async () => {
    let dropdown = await browser.$('#dropdown');
    expect(await dropdown.getValue()).toBe('2');
});

When(/^Perform dropdown interaction - select option 1 of 2$/, async () => {
    let dropdownArr = await browser.$$('#dropdown > option');
    for (let i = 0; i < (await dropdownArr.length); i++) {
        if (i === 1) {
            await dropdownArr[i].click();
            break;
        }
    }
});

Then(/^The new dropdown value should be 1 again$/, async () => {
    let dropdown = await browser.$('#dropdown');
    expect(await dropdown.getValue()).toBe('1');
});

// checkbox interactions
Given(/^Checkbox page is open$/, async () => {
    await browser.url('https://the-internet.herokuapp.com/checkboxes');
    await browser.setTimeout({ implicit: 15000, pageLoad: 10000 });
    await browser.maximizeWindow();
});

When(/^Check selected checkbox value$/, async () => {
    let checkboxArr = await browser.$$('#checkboxes > input[type="checkbox"]');
    for (let i = 0; i < (await checkboxArr.length); i++) {
        if (i === 0) {
            let value = await checkboxArr[i].isSelected();
            expect(value).toBe(false);
        }

        if (i === 1) {
            let value = await checkboxArr[i].isSelected();
            expect(value).toBe(true);
        }
    }
});

When(/^Perform checkbox interaction - select unselected checkbox$/, async () => {
    let checkboxArr = await browser.$$('#checkboxes > input[type="checkbox"]');
    for (let i = 0; i < (await checkboxArr.length); i++) {
        if ((await checkboxArr[i].isSelected()) === false) {
            await checkboxArr[i].click();
            break;
        }
    }
});

Then(/^The first checkbox value should be true$/, async () => {
    let checkboxArr = await browser.$$('#checkboxes > input[type="checkbox"]');
    expect(await checkboxArr[0].isSelected()).toBe(true);
});

// scroll and screenshot
Given(/^eCommerce web page is open$/, async () => {
    await browser.url('https://www.amazon.de');
    await browser.setTimeout({ implicit: 15000, pageLoad: 10000 });
    await browser.maximizeWindow();
    browser.pause(10000);
});

When(/^Scroll to the bottom of the page$/, async () => {
    await browser.execute(() => {
        window.scrollTo(0, document.body.scrollHeight);
    });
    browser.pause(10000);
});

Then(/^Take a screenshot of the page$/, async () => {
    // check if dir exists else create it
    if (!fs.existsSync('./screenshots')) {
        fs.mkdirSync('./screenshots', { recursive: true });
    }
    await browser.saveScreenshot('./screenshots/screenshot.png');
    browser.pause(10000);
});

// window interactions
Given(/^Web page is open$/, async () => {
    await browser.url('https://the-internet.herokuapp.com/windows');
    await browser.waitUntil(
        async () => {
            return (await browser.execute(() => document.readyState)) === 'complete';
        },
        { timeout: 15000, timeoutMsg: 'Page not loaded' }
    );
    await browser.maximizeWindow();
});

When(/^Check webpage is completely loaded by listening for DOM content to be loaded$/, async () => {
    await browser.waitUntil(
        async () => {
            return (await browser.execute(() => document.readyState)) === 'complete';
        },
        { timeout: 15000, timeoutMsg: 'Page not loaded' }
    );
    await browser.pause(1000);
});

When(/^Open another window$/, async () => {
    let link = await browser.$('a[href="http://elementalselenium.com/"]');
    await link.click();
    await browser.waitUntil(
        async () => {
            return (await browser.execute(() => document.readyState)) === 'complete';
        },
        { timeout: 15000, timeoutMsg: 'Page not loaded' }
    );
    const windowHandles = await browser.getWindowHandles();
    expect(windowHandles.length).toBe(2);
});

Then(/^Browser should have two windows$/, async () => {
    const windowHandles = await browser.getWindowHandles();
    expect(windowHandles.length).toBe(2);
});

When(/^Switch back to old window$/, async () => {
    await browser.switchWindow(/^The Internet(.*)/);
    await browser.pause(1000);
});

Then(/^Check the title of the window to be The Internet$/, async () => {
    const title = await browser.getTitle();
    expect(title).toBe('The Internet');
});

When(/^Switch to window based on title$/, async () => {
    await browser.switchWindow('Home | Elemental Selenium');
    await browser.pause(1000);
});

Then(/^Check the title of the window to be Home | Elemental Selenium$/, async () => {
    const title = await browser.getTitle();
    await browser.pause(1000);
    expect(title).toBe('Home | Elemental Selenium');
});

When(/^Switch back to the main window$/, async () => {
    await browser.switchWindow('The Internet');
    await browser.pause(1000);
    const title = await browser.getTitle();
    expect(title).toBe('The Internet');
});
